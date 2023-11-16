# from django.http import JsonResponse
# from .models import Village
#
# def village_list(request):
#     villages = Village.objects.all().values()
#     return JsonResponse(list(villages), safe=False)
#
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView

from .buildings_data import buildings
from .forms import UserLoginForm
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

from .tasks import update_resources


class UserLoginView(LoginView):
    # ... twoja konfiguracja klasy ...
    success_url = reverse_lazy('plemiona:plemiona')  # Użyj przestrzeni nazw 'plemiona' # ścieżka do Twojego szablonu logowania


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
    map_size = 11
    game_map = [[" " for _ in range(map_size)] for _ in range(map_size)]

    villages = Village.objects.all()
    for village in villages:
        if 0 <= village.coordinate_x < map_size and 0 <= village.coordinate_y < map_size:
            game_map[village.coordinate_y][village.coordinate_x] = village
    print(game_map)
    context = {
        'game_map': game_map,  # Załóżmy, że game_map to twoja mapa gry
        'active_village_id': active_village_id
    }
    return render(request, 'plemiona/map.html', context)

# ratusz z opcjami z rozbudowa itd
def town_hall_view(request, village_id):
    village = Village.objects.get(id=village_id, user=request.user)
    missing_resources = []
    next_levels = {}
    building_levels = {}
    for building in buildings:
        current_level = getattr(village, building)
        next_level_data = next((item for item in buildings[building] if item["lvl"] == current_level + 1), None)
        next_levels[building] = next_level_data
        building_levels[building] = current_level
    print("dane")
    print(next_levels)
    print(building_levels)
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
    building_data = buildings[building_type]
    next_level_data = next((item for item in building_data if item["lvl"] == current_level + 1), None)

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