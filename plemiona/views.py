# from django.http import JsonResponse
# from .models import Village
#
# def village_list(request):
#     villages = Village.objects.all().values()
#     return JsonResponse(list(villages), safe=False)
#
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView

from .army_data import army_data
# from .buildings_data import buildings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from .models import Village
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
import random
from django.db import IntegrityError
from .forms import CustomLoginForm
from .scipts_logic.attack_logic import simulate_battle
from .scipts_logic.loot_from_village import calculate_loot
from .buildings_data.buildings import buildings_data_dict
from .tasks import update_resources


# class UserLoginView(LoginView):
#     # ... twoja konfiguracja klasy ...
#     success_url = reverse_lazy('plemiona:plemiona')  # Użyj przestrzeni nazw 'plemiona' # ścieżka do Twojego szablonu logowania
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'plemiona/login.html'

@staff_member_required
def admin_create_village(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        village_name = request.POST.get('village_name')
        user = User.objects.get(id=user_id)
        new_village = Village(user=user, village_name=village_name)
        new_village.save()
        # return redirect('plemiona:admin/create_village.html')  # Przekieruj po utworzeniu wioski

    users = User.objects.all()
    a="czym ja jestem?"
    return render(request, 'plemiona/admin_create_village.html', {'users': users, 'infos':a})

@login_required
def get_user_village(request):
    user_villages = Village.objects.filter(user=request.user)
    if not request.session.get('active_village'):
        user_villages = Village.objects.filter(user=request.user)
        if user_villages.exists():
            request.session['active_village'] = user_villages.first().id

            request.session['active_village_full']  = 7
    print(request.session.get('active_village'))
    print(request.session.get('active_village_full'))
    return render(request, 'plemiona/user_villages.html', {'villages': user_villages})

# w pliku views.py twojej aplikacji


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plemiona:get_user_village')  # Zmień na odpowiedni URL
    else:
        form = UserRegisterForm()
    return render(request, 'plemiona/register.html', {'form': form})


def create_village_for_user(username):
    # Znajdź użytkownika na podstawie nazwy użytkownika
    village_name = f'New_{username}'
    user = User.objects.get(username=username)

    # Generuj unikalne koordynaty
    unique_coordinates = False
    while not unique_coordinates:
        coordinate_x = random.randint(1, 10)  # Zakładając, że chcesz koordynaty od 1 do 10
        coordinate_y = random.randint(1, 10)
        if not Village.objects.filter(coordinate_x=coordinate_x, coordinate_y=coordinate_y).exists():
            unique_coordinates = True

    # Utwórz nową wioskę
    new_village = Village(
        user=user,
        village_name=village_name,
        coordinate_x=coordinate_x,
        coordinate_y=coordinate_y,
        # Ustaw pozostałe wartości na podstawie domyślnych wartości modelu Village
        town_hall=1,
        barracks=0,
        pikemen=0,
        halberdiers=0
    )

    # Zapisz wioskę w bazie danych
    try:
        new_village.save()
        return new_village
    except IntegrityError:
        # W przypadku, gdyby doszło do kolizji koordynatów pomimo sprawdzenia
        return None


# Tworzenie mapy do gry

from django.shortcuts import render
from .models import Village

from django.shortcuts import get_object_or_404, render
from .models import Village

def village_detail(request, village_id):
    village = get_object_or_404(Village, id=village_id)

    # Sprawdź, czy wioska należy do zalogowanego użytkownika
    if village.user == request.user:
        # Ustaw tę wioskę jako aktywną w sesji
        request.session['active_village'] = village.id
    else:
        # Jeśli wioska nie należy do użytkownika, nie zmieniaj active_village
        pass
    return render(request, 'plemiona/village_detail.html', {'village': village})

def map_view(request):
    active_village_id = request.session.get('active_village')
    if active_village_id:
        active_village = Village.objects.get(id=active_village_id)
        # Użyj active_village do czegoś
    else:
        #TODO ale sie nie powinno zdarzyć
    # Obsługa przypadku, gdy aktywna wioska nie jest ustawiona
        user_villages = Village.objects.filter(user=request.user)
    map_size = 100
    game_map = [[" " for _ in range(map_size)] for _ in range(map_size)]

    villages = Village.objects.all()
    for village in villages:
        if 0 <= village.coordinate_x < map_size and 0 <= village.coordinate_y < map_size:
            game_map[village.coordinate_y][village.coordinate_x] = village
    print(game_map)
    num_columns = len(game_map[0]) if game_map else 0
    column_numbers = list(range(num_columns))
    game_map_with_row_numbers = [(row_num, row) for row_num, row in enumerate(game_map)]

    context = {
        'game_map': game_map_with_row_numbers,  # Załóżmy, że game_map to twoja mapa gry
        'active_village_id': active_village_id,
        'column_numbers': column_numbers,
    }
    return render(request, 'plemiona/map.html', context)

# ratusz z opcjami z rozbudowa itd
def town_hall_view(request, village_id):
    village = Village.objects.get(id=village_id, user=request.user)
    missing_resources = []
    next_levels = {}
    building_levels = {}
    for building, levels in buildings_data_dict.items():
        current_level = getattr(village, building)
        next_level_data = levels.get(current_level + 1)
        next_levels[building] = next_level_data
        building_levels[building] = current_level
    # print("dane")
    # print(next_levels)
    # print(building_levels)
    missing_resources = request.session.pop('missing_resources', None)
    context = {
        'village': village,
        'next_levels': next_levels,
        'building_levels': building_levels,
        'missing_resources': missing_resources
    }
    return render(request, 'plemiona/town_hall.html', context)


# napisz mi funkcje, która będzie rozbudowywała budynek pobierała z tabeli village poziom np tartaku i sprawdzała z danych w buildings_data.py ile
# kosztuje wyższy poziom i pobierze to z village i rozbuduje o 1 budynek



def upgrade_building(request, village_id, building_type):
    # Pobierz wioskę
    village = get_object_or_404(Village, id=village_id, user=request.user)
    # Pobierz obecny poziom budynku
    current_level = getattr(village, building_type)

    # Pobierz dane budynku dla następnego poziomu
    building_data = buildings_data_dict.get(building_type, {})
    next_level_data = building_data.get(current_level + 1)
    print(current_level)
    print(building_data)
    print(next_level_data)

    if not next_level_data:
        # Przekieruj z powrotem do town_hall z komunikatem o błędzie
        return redirect('plemiona:town_hall_view', village_id=village_id)

    # Sprawdź, czy wioska ma wystarczające zasoby
    if (
            village.wood >= next_level_data["wood"]
            and village.clay >= next_level_data["clay"]
            and village.iron >= next_level_data["iron"]):
        # Odejmij zasoby i zwiększ poziom budynku
        village.wood -= next_level_data["wood"]
        village.clay -= next_level_data["clay"]
        village.iron -= next_level_data["iron"]
        setattr(village, building_type, current_level + 1)
        village.save()
        # Przekieruj z powrotem do town_hall z komunikatem o sukcesie
        return redirect('plemiona:town_hall_view', village_id=village_id)
    else:
        # Przekieruj z powrotem do town_hall z komunikatem o braku zasobów
        missing_resources = []
        if village.wood < next_level_data['wood']:
            missing_resources.append('drewno')
        if village.clay < next_level_data['clay']:
            missing_resources.append('glina')
        if village.iron < next_level_data['iron']:
            missing_resources.append('żelazo')

        if missing_resources:

            request.session['missing_resources'] = missing_resources
            return redirect('plemiona:town_hall_view', village_id=village_id)

#

# @login_required2
def barracks_view(request, village_id):
    village = Village.objects.get(id=village_id, user=request.user)
    missing_resources_units = []
    current_army = {
        'pikemen': village.pikemen,
        'halberdiers': village.halberdiers,
        'axeman': village.axeman,
        'archer': village.archer,
    }
    missing_resources_units = request.session.pop('missing_resources_units', None)
    context = {
        'village': village,
        'army_data': army_data,
        'current_army': current_army,
        'missing_resources_units': missing_resources_units
    }
    # sprawdzić dalczego nie działa "current_army"

    return render(request, 'plemiona/barracks.html', context)

@login_required
def recruit_units(request, village_id):
    if request.method == 'POST':
        village = Village.objects.get(id=village_id, user=request.user)

        total_wood_needed = 0
        total_clay_needed = 0
        total_iron_needed = 0

        for unit, costs in army_data.items():
            quantity_key = f'quantity_{unit}'
            quantity = int(request.POST.get(quantity_key, 0))
            # print(quantity_key,quantity)
            if quantity > 0:
                wood_needed = costs['wood'] * quantity
                clay_needed = costs['clay'] * quantity
                iron_needed = costs['iron'] * quantity

                total_wood_needed += wood_needed
                total_clay_needed += clay_needed
                total_iron_needed += iron_needed

                # Tutaj możesz dodać logikę sprawdzającą, czy wioska ma wystarczająco surowców
                # i ewentualnie przeprowadzić rekrutację
        print(total_wood_needed, total_clay_needed, total_iron_needed)
                # Sprawdzenie, czy wystarcza surowców
        if (
                village.wood >= total_wood_needed
                and village.clay >= total_clay_needed
                and village.iron >= total_iron_needed):
                for unit, costs in army_data.items():

                        quantity_key = f'quantity_{unit}'
                        quantity = int(request.POST.get(quantity_key, 0))
                        print(quantity_key,quantity,unit)

                        if quantity > 0:
                            # Aktualizacja liczby jednostek w wiosce
                            current_quantity = getattr(village, unit, 0)
                            setattr(village, unit, current_quantity + quantity)
                            print(village,unit,current_quantity,quantity)
                    # Logika rekrutacji
                    # Aktualizacja surowców w wiosce
                        village.wood -= total_wood_needed
                        village.clay -= total_clay_needed
                        village.iron -= total_iron_needed
                        village.save()
                    # Przekierowanie po pomyślnej rekrutacji
                return redirect('plemiona:barracks_view', village_id=village_id)
        else:
                    # Przekieruj z powrotem do town_hall z komunikatem o braku zasobów
                    missing_resources_units = []
                    if village.wood < total_wood_needed:
                        missing_resources_units.append('drewno')
                    if village.clay < total_clay_needed:
                        missing_resources_units.append('glina')
                    if village.iron < total_iron_needed:
                        missing_resources_units.append('żelazo')

                    if missing_resources_units:
                        request.session['missing_resources_units'] = missing_resources_units
                        return redirect('plemiona:barracks_view', village_id=village_id)


            # Przekierowanie do formularza rekrutacji w przypadku żądania innego niż POST
        return redirect('plemiona:barracks_view', village_id=village_id)


def place_view(request,village_id):

        village = Village.objects.get(id=village_id, user=request.user)
        missing_units = []

        missing_resources_units = request.session.pop('missing_units', None)
        context = {
            'village': village,
            'army_data': army_data,
            'missing_units': missing_resources_units
        }
        # sprawdzić dalczego nie działa "current_army"
        return render(request, 'plemiona/place.html', context)




@login_required
def attack_view(request, village_id):
    if request.method == 'POST':
        attacker_village = get_object_or_404(Village, id=village_id)
        x_coordinate = request.POST.get('coordinate_x')
        y_coordinate = request.POST.get('coordinate_y')
        defender_village = get_object_or_404(Village, coordinate_x=x_coordinate, coordinate_y=y_coordinate)
        # logic to take units from form and use them in function
        units_to_attack = {}
        for key in request.POST:
            if key.startswith('quantity-'):
                unit_name = key.split('-')[1]  # Pobranie nazwy jednostki
                quantity = int(request.POST.get(key, 0))  # Pobranie ilości jednostek
                if quantity > 0:
                    units_to_attack[unit_name] = quantity

        print("Wspolrzedne X i Y:", x_coordinate, y_coordinate)
        print("Jednostki do ataku:", units_to_attack)

        #  take units from defender village
        unit_names = list(army_data.keys())
        defender_units = {unit: getattr(defender_village, unit,0) for unit in unit_names }
        defender_units = {k: v for k, v in defender_units.items() if v != 0}
        print("Jednostki w wiosce obroncy:", defender_units)
        defender_units={"halberdiers": 8,'archer':15}
        units_to_attack = {"axeman": 100, 'light_cavalry': 5}
        battle_result = {'axeman': 80, 'light_cavalry': 4}
        winner,battle_result = simulate_battle(units_to_attack, defender_units, army_data)
        # Aktualizacja danych po walce
        print(winner,battle_result)

        update_units_after_battle(attacker_village.id,defender_village.id,units_to_attack,defender_units, winner,battle_result)

        return redirect('plemiona:place_view', village_id=village_id)
        print("udalo sie")
    else:
        return render(request, 'attack_form.html', {'village_id': village_id})
        print("nie udalo sie")


from django.db import transaction

def update_units_after_battle(attacker_village_id, defender_village_id, units_to_attack, defender_units, winner, battle_result):
    with transaction.atomic():
        # Pobierz wioski
        attacker_village = Village.objects.get(id=attacker_village_id)
        defender_village = Village.objects.get(id=defender_village_id)

        if winner == 'attacker':
            # Atakujący wygrywa
            for unit, count in units_to_attack.items():
                loss = count - battle_result.get(unit, 0)
                current_count = getattr(attacker_village, unit, 0)
                setattr(attacker_village, unit, max(current_count - loss, 0))

            for unit, count in defender_units.items():
                current_count = getattr(defender_village, unit, 0)
                setattr(defender_village, unit, max(current_count - count, 0))
            calculate_loot(battle_result, army_data, defender_village,attacker_village)
        else:
            # Obrońca wygrywa
            for unit, count in units_to_attack.items():
                current_count = getattr(attacker_village, unit, 0)
                setattr(attacker_village, unit, max(current_count - count, 0))

            for unit, count in defender_units.items():
                loss = count - battle_result.get(unit, 0)
                current_count = getattr(defender_village, unit, 0)
                setattr(defender_village, unit, max(current_count - loss, 0))

        # Zapisz zmiany w bazie danych
        attacker_village.save()
        defender_village.save()

