# from django.http import JsonResponse
# from .models import Village
#
# def village_list(request):
#     villages = Village.objects.all().values()
#     return JsonResponse(list(villages), safe=False)
#
from django.contrib.auth.views import LoginView
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
class UserLoginView(LoginView):
    # ... twoja konfiguracja klasy ...
    success_url = reverse_lazy('plemiona:plemiona')  # Użyj przestrzeni nazw 'plemiona' # ścieżka do Twojego szablonu logowania


@login_required
def get_user_village(request):
    village = Village.objects.get(user=request.user)
    data = {
        'village_name': village.village_name,
        'coordinate_x': village.coordinate_x,
        'coordinate_y': village.coordinate_y,
        'town_hall': village.town_hall,
        'barracks': village.barracks,
        'pikemen': village.pikemen,
        'halberdiers': village.halberdiers,
    }
    return JsonResponse(data)

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

# def add_village_to_user(username):
#     # Znajdź użytkownika na podstawie podanej nazwy
#     user = User.objects.get(username=username)
#
#     # Utwórz nową wioskę z unikalnymi koordynatami
#     while True:
#         x = random.randint(1, 10)  # Zakładając, że chcesz koordynaty od 1 do 10
#         y = random.randint(1, 10)
#         if not Village.objects.filter(coordinate_x=x, coordinate_y=y).exists():
#             new_village = Village(user=user, coordinate_x=x, coordinate_y=y)
#             new_village.save()
#             break
#         else:
#             # Jeśli koordynaty nie są unikalne, spróbuj ponownie
#             continue
#
#     return new_village

def create_village_for_user(username, village_name='New Village333'):
    # Znajdź użytkownika na podstawie nazwy użytkownika
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