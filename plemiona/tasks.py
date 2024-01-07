from celery import shared_task
from django.db import transaction
from django.utils import timezone

from djangoProject1.celery import app
from .army_data import army_data
from .buildings_data.buildings import buildings_data_dict
# from .buildings_data import buildings
from .models import Village, BuildingProperties, BuildingTask, ArmyTask, ResearchTask
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