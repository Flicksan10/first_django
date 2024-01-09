from celery import shared_task
from django.db import transaction
from django.utils import timezone

from djangoProject1.celery import app
from .army_data import army_data
from .buildings_data.buildings import buildings_data_dict
# from .buildings_data import buildings
from .models import Village, BuildingProperties, BuildingTask, ArmyTask, ResearchTask, RecruitmentOrder
from .scipts_logic.after_battle_return import create_return_task
from .scipts_logic.attack_logic import simulate_battle
from .scipts_logic.after_battle_logic import update_units_after_battle
from .scipts_logic.return_attack_logic import handle_return_attack

import logging



# @shared_task
@app.task
def update_resources():
    with transaction.atomic():
        # print("dziam")
        villages = Village.objects.all()
        for village in villages:
            # Zakładając, że masz funkcję do pobierania wydajności na podstawie poziomu
            wood_increase = get_performance(village.sawmill, 'sawmill', buildings_data_dict['sawmill'])
            clay_increase = get_performance(village.clay_pit, 'clay_pit', buildings_data_dict['clay_pit'])
            iron_increase = get_performance(village.iron_mine, 'iron_mine', buildings_data_dict['iron_mine'])

            village.resources.wood += wood_increase
            village.resources.clay += clay_increase
            village.resources.iron += iron_increase
            village.resources.save()

def get_performance(level, building_type, resource_data):
    # level -= 1  # Dostosowanie poziomu indeksowanie rozpoczyna się od 0

    if building_type == 'sawmill':
        # print(resource_data[level]["performance"])
        data = resource_data[level]["performance"] / 360
    elif building_type == 'clay_pit':
        data = resource_data[level]["performance"] / 360
    elif building_type == 'iron_mine':
        data = resource_data[level]["performance"] / 360
    else:
        raise ValueError("Nieznany typ budynku")

    return data
# @app.task
# def update_resources():
#     with transaction.atomic():
#         villages = Village.objects.all()
#         for village in villages:
#             # Pobierz właściwości tylko dla interesujących nas budynków
#             properties = BuildingProperties.objects.filter(
#                 village=village,
#                 building_type__in=['sawmill', 'clay_pit', 'iron_mine']
#             )
#
#             # Inicjalizacja zmiennych
#             wood_increase = 0
#             clay_increase = 0
#             iron_increase = 0
#
#             # Obliczanie wzrostu zasobów
#             for prop in properties:
#                 if prop.building_type == 'sawmill':
#                     wood_increase += prop.performance/ 360
#                 elif prop.building_type == 'clay_pit':
#                     clay_increase += prop.performance/ 360
#                 elif prop.building_type == 'iron_mine':
#                     iron_increase += prop.performance/ 360
#
#             # Aktualizacja zasobów wioski
#             village.wood += wood_increase
#             village.clay += clay_increase
#             village.iron += iron_increase
#             village.save()


# @app.task
# def update_resources():
#     with transaction.atomic():
#         villages = Village.objects.select_related('resources').all()
#         for village in villages:
#             # Pobierz właściwości tylko dla interesujących nas budynków
#             properties = BuildingProperties.objects.filter(
#                 village=village,
#                 building_type__in=['sawmill', 'clay_pit', 'iron_mine']
#             )
#
#             # Inicjalizacja zmiennych
#             wood_increase = 0
#             clay_increase = 0
#             iron_increase = 0
#
#             # Obliczanie wzrostu zasobów
#             for prop in properties:
#                 if prop.building_type == 'sawmill':
#                     wood_increase += prop.performance / 360
#                 elif prop.building_type == 'clay_pit':
#                     clay_increase += prop.performance / 360
#                 elif prop.building_type == 'iron_mine':
#                     iron_increase += prop.performance / 360
#
#             # Aktualizacja zasobów wioski
#             resources = village.resources
#             resources.wood += wood_increase
#             resources.clay += clay_increase
#             resources.iron += iron_increase
#             resources.save()

@app.task
def check_building_tasks():
    with transaction.atomic():
    # Przeszukaj aktywne zadania, które powinny być już zakończone
        for task in BuildingTask.objects.filter(completion_time__lte=timezone.now(), is_active=True):
            village = task.village

            # Aktualizuj poziom budynku w Village
            setattr(village, task.building_type, task.target_level)
            village.save()
            # Usuń wykonane zadanie
            task.delete()

            # Aktywuj kolejne zadanie, jeśli istnieje
            next_task = BuildingTask.objects.filter(village=task.village, is_active=False).order_by('completion_time').first()
            if next_task:
                next_task.is_active = True
                next_task.save()

@app.task
def process_attacks():
    with transaction.atomic():
        for task in ArmyTask.objects.filter(arrival_time__lte=timezone.now()):
            attacker_village = task.attacker_village
            defender_village = task.defender_village
            defender_army = defender_village.army
            units_to_attack = task.army_composition

            if task.action_type == 'attack':
                # Pobierz jednostki obrońcy z modelu Army
                defender_units = {}
                for unit in army_data.keys():
                    inside_units = getattr(defender_army, f"{unit}_inside", 0)
                    defender_units[unit] = inside_units

                # Symuluj bitwę
                winner, battle_result = simulate_battle(units_to_attack, defender_units, army_data)

                # Aktualizuj dane po walce
                update_units_after_battle(attacker_village.id, defender_village.id, units_to_attack, defender_units,
                                          winner, battle_result)

                # Usuń zadanie ataku
                task.delete()

            elif task.action_type == 'return_attack':
                handle_return_attack(task)

@app.task
def check_research_tasks():
    with transaction.atomic():
        for task in ResearchTask.objects.filter(completion_time__lte=timezone.now(), is_active=True):
            village = task.village

            # Update the research status in the Research model

            setattr(village, task.research_type, True)
            village.save()
            # Usuń wykonane zadanie
            task.delete()

            # Activate the next task, if exists
            next_task = ResearchTask.objects.filter(village=task.village, is_active=False).order_by('completion_time').first()
            if next_task:
                next_task.is_active = True
                next_task.save()



@app.task
def process_recruitment_orders():
    with transaction.atomic():
        # Pobierz aktywne zamówienia, które są gotowe do przetworzenia
        active_orders = RecruitmentOrder.objects.filter(is_active=True,unit_recruit_time__lte=timezone.now())
        for order in active_orders:
            village = order.village
            barracks_performance = buildings_data_dict['barracks'][village.barracks]['performance']

            if order.quantity > 0:
                army = village.army
                unit_inside_field = f'{order.unit_type}_inside'
                current_quantity = getattr(army, unit_inside_field, 0)
                setattr(army, unit_inside_field, current_quantity + 1)
                army.save()

                order.quantity -= 1
                if order.quantity == 0:
                    order.delete()
                else:
                    # Oblicz czas rekrutacji dla kolejnej jednostki
                    unit_recruit_time = army_data[order.unit_type]['recruit_time'] *  ( barracks_performance/100)
                    # Ustaw czas rozpoczęcia kolejnej jednostki za kazdym razme ma byc sprawdzone kiedy zakonczy sie rekrutacja
                    order.single_unit_recruit_time = timezone.now() + timezone.timedelta(seconds=unit_recruit_time)
                    order.save()

            # chce aby było to najstarsze zadanie ma ono byc pobrane dopiero jesli zostanie usuniete poprzednie
            next_order = RecruitmentOrder.objects.filter(village=village, is_active=False).order_by('created_data').first()
            if next_order:
                next_order.is_active = True
                # Zaktualizuj czas rekrutacji dla następnego zamówienia
                next_unit_recruit_time = army_data[next_order.unit_type]['recruit_time']
                adjusted_next_recruit_time = next_unit_recruit_time * ( barracks_performance / 100 )
                next_order.single_unit_recruit_time = timezone.now() + timezone.timedelta(seconds=adjusted_next_recruit_time)
                next_order.save()

