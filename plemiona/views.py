# from django.http import JsonResponse
# from .models import Village
#
# def village_list(request):
#     villages = Village.objects.all().values()
#     return JsonResponse(list(villages), safe=False)
#
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Village
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
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

