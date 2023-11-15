# from django.http import JsonResponse
# from .models import Village
#
# def village_list(request):
#     villages = Village.objects.all().values()
#     return JsonResponse(list(villages), safe=False)
#
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView

from .buildings_data import town_hall
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
    print("eeasd")
    village = get_object_or_404(Village, id=village_id)
    return render(request, 'plemiona/village_detail.html', {'village': village})

def map_view(request):
    map_size = 10
    game_map = [[" " for _ in range(map_size)] for _ in range(map_size)]

    villages = Village.objects.all()
    for village in villages:
        if 0 <= village.coordinate_x < map_size and 0 <= village.coordinate_y < map_size:
            game_map[village.coordinate_y][village.coordinate_x] = village

    return render(request, 'plemiona/map.html', {'game_map': game_map})

# ratusz z opcjami z rozbudowa itd
def town_hall_view(request, village_id):
    # Użyj village_id do pobrania konkretnej wioski
    village = Village.objects.get(id=village_id)

    current_town_hall_data = next((item for item in town_hall if item["lvl"] == village.town_hall), None)
    context = {
        'village': village,
        'buildings_data': current_town_hall_data
    }
    print("halo")
    return render(request, 'plemiona/town_hall.html', context)


def upgrade_building(request, building):
    # Logika rozbudowy budynku
    # ...
    print("policja")
    return redirect('town_hall')  # Przekieruj z powrotem do widoku town_hall
