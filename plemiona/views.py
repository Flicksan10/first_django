# from django.http import JsonResponse
# from .models import Village
#
# def village_list(request):
#     villages = Village.objects.all().values()
#     return JsonResponse(list(villages), safe=False)
#
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView
from django.db.models import Q, Max

from .army_data import army_data
# from .buildings_data import buildings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .buildings_data.building_req_function import check_building_requirements
from .buildings_data.building_requirements import buildings_lvl_requirements
from .buildings_data.create_village_scripts import \
    initialize_building_properties_new_village, calculate_performance_building
from .buildings_data.inicialization_script import initialize_building_properties, create_resources_for_all_villages, \
    initialize_army_for_all_villages
from .models import Topic_message, Notification, Answers_Message, Reports, BuildingProperties, VillageResources, \
    BuildingTask, ArmyTask, Army, ResearchTask, Research
from .forms import MessageForm
from .models import Village
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
import random
from django.db import IntegrityError
from .forms import CustomLoginForm
from .research.research_requirements import units
from .scipts_logic.after_battle_logic import save_battle_report
from .scipts_logic.after_battle_return import calculate_travel_time
from .scipts_logic.attack_logic import simulate_battle
from .scipts_logic.loot_from_village import calculate_loot
from .buildings_data.buildings import buildings_data_dict
from .tasks import update_resources
from django.contrib import messages

# class UserLoginView(LoginView):
#     # ... twoja konfiguracja klasy ...
#     success_url = reverse_lazy('plemiona:plemiona')  # Użyj przestrzeni nazw 'plemiona' # ścieżka do Twojego szablonu logowania
# create_resources_for_all_villages()
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
            create_village_for_user(user.username)
            # Tworzenie wioski dla nowego użytkownika
            return redirect('plemiona:login')  # Zmień na odpowiedni URL
    else:
        form = UserRegisterForm()
    return render(request, 'plemiona/register.html', {'form': form})


def create_village_for_user(username):
    # Znajdź użytkownika na podstawie nazwy użytkownika
    user = User.objects.get(username=username)
    # Generuj nazwę wioski
    village_name = f'New_{username}'
    # Utwórz nową wioskę z właściwościami
    new_village = create_village_with_properties(village_name, user)
    return new_village

def create_village_with_properties(village_name, user):
    # Generuj unikalne koordynaty
    unique_coordinates = False
    while not unique_coordinates:
        coordinate_x = random.randint(1, 10)  # Zakładając, że chcesz koordynaty od 1 do 10
        coordinate_y = random.randint(1, 10)
        if not Village.objects.filter(coordinate_x=coordinate_x, coordinate_y=coordinate_y).exists():
            unique_coordinates = True
            # Utwórz nową wioskę
            village = Village.objects.create(
                user=user,
                village_name=village_name,
                coordinate_x=coordinate_x,
                coordinate_y=coordinate_y,
            )
            # Inicjalizuj właściwości budynków dla nowej wioski
            initialize_building_properties_new_village(village)
            VillageResources.objects.create(village=village)
            Army.objects.create(village=village)
            Research.objects.create(village=village)
            # ResearchTask.objects.create(village=village)
            return village

    # W przypadku, gdyby nie udało się znaleźć unikalnych koordynatów
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
        army_tasks = ArmyTask.objects.filter(attacker_village=village)
    else:
        army_tasks = None
        pass
    return render(request, 'plemiona/village_detail.html', {'village': village, 'army_tasks': army_tasks})

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
    building_tasks = BuildingTask.objects.filter(village=village)
    town_hall_level = getattr(village, 'town_hall')
    town_hall_performance = buildings_data_dict['town_hall'][town_hall_level]['performance']

    missing_resources = []
    next_levels = {}
    building_levels = {}
    building_tasks_data = {}
    building_tasks_data_list = []

    # Przygotowanie danych o zadaniach budowy

    for building, levels in buildings_data_dict.items():
        current_level = getattr(village, building)
        highest_target_level = building_tasks_data.get(building, current_level)
        next_level_data = levels.get(highest_target_level + 1)

        if next_level_data:
            total_resources_cost = next_level_data["wood"] + next_level_data["clay"] + next_level_data["iron"]
            build_time_seconds = round((total_resources_cost * town_hall_performance) / 100)
            build_time_formatted = convert_seconds_to_time(build_time_seconds)
            next_level_data = next_level_data.copy()
            next_level_data['build_time'] = build_time_formatted

        next_levels[building] = next_level_data
        building_levels[building] = current_level
    error_message = request.session.pop('error_message', None)
    missing_resources = request.session.pop('missing_resources', None)
    for task in building_tasks:
        building_tasks_data_list.append({
            'building_type': task.building_type,
            'target_level': task.target_level,
            'completion_time': task.completion_time,
            'is_active': task.is_active
        })
    context = {
        'village': village,
        'next_levels': next_levels,
        'building_levels': building_levels,
        'missing_resources': missing_resources,
        'error_message': error_message,
        'building_tasks': building_tasks_data_list  # Dodaj dane o zadaniach budowy do kontekstu
    }

    return render(request, 'plemiona/town_hall.html', context)

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours}h {minutes}min {remaining_seconds}s"


    # print("Total population for next level:", next_level_data.get("total_population", "N/A"))
    # print("People needed for next level:", next_level_data.get("people_needed", "N/A"))


from django.utils import timezone

def upgrade_building(request, village_id, building_type):
    village = get_object_or_404(Village, id=village_id, user=request.user)
    current_level = getattr(village, building_type)
    building_data = buildings_data_dict.get(building_type, {})
    lvl_requirements = buildings_lvl_requirements
    meets_requirements, message = check_building_requirements(village, building_type, lvl_requirements)
    if not meets_requirements:
        # Handle the case where requirements are not met
        # For example, send a message back to the user
        request.session['error_message'] = f"Nie spelniono Wymagan {message}"
        return redirect('plemiona:town_hall_view', village_id=village_id)

    tasks_count = BuildingTask.objects.filter(village=village).count()
    if tasks_count >= 3:
        request.session['error_message'] = "Limit zadań osiągnięty."
        # Przekieruj z powrotem z komunikatem o osiągnięciu limitu zadań
        return redirect('plemiona:town_hall_view', village_id=village_id)

    # Znajdź ostatnie zadanie w kolejce
    last_task = BuildingTask.objects.filter(village=village).order_by('-completion_time').first()
    start_time = last_task.completion_time if last_task else timezone.now()

    # Ustal poziom docelowy dla nowego zadania
    highest_target_level = BuildingTask.objects.filter(
        village=village,
        building_type=building_type
    ).aggregate(Max('target_level'))['target_level__max']
    target_level = highest_target_level + 1 if highest_target_level is not None else current_level + 1

    # Pobierz dane budynku dla poziomu docelowego
    target_level_data = building_data.get(target_level)
    if not target_level_data:
        return redirect('plemiona:town_hall_view', village_id=village_id)

    if (village.resources.wood >= target_level_data["wood"] and
            village.resources.clay >= target_level_data["clay"] and
            village.resources.iron >= target_level_data["iron"]):
        print(target_level,target_level_data["wood"],target_level_data["clay"],target_level_data["iron"] )

        # Oblicz czas budowy
        total_resources_cost = target_level_data["wood"] + target_level_data["clay"] + target_level_data["iron"]
        town_hall_performance = buildings_data_dict['town_hall'][village.town_hall]['performance']
        build_time_seconds = round((total_resources_cost * town_hall_performance) / 100)
        completion_time = start_time + timezone.timedelta(seconds=build_time_seconds)

        # Odejmij zasoby
        village.resources.wood -= target_level_data["wood"]
        village.resources.clay -= target_level_data["clay"]
        village.resources.iron -= target_level_data["iron"]
        village.resources.save()

        is_active = tasks_count == 0
        # Zapisanie zadania budowy w tabeli
        BuildingTask.objects.create(
            village=village,
            building_type=building_type,
            target_level=target_level,
            completion_time=completion_time,
            is_active=is_active
        )

        return redirect('plemiona:town_hall_view', village_id=village_id)

    else:
        # Przekieruj z powrotem do town_hall z komunikatem o braku zasobów
        missing_resources = []
        if village.resources.wood < target_level_data['wood']:
            missing_resources.append('drewno')
        if village.resources.clay < target_level_data['clay']:
            missing_resources.append('glina')
        if village.resources.iron < target_level_data['iron']:
            missing_resources.append('żelazo')

        if missing_resources:
            request.session['missing_resources'] = missing_resources
            return redirect('plemiona:town_hall_view', village_id=village_id)


#

# @login_required2
def barracks_view(request, village_id):
    village = Village.objects.get(id=village_id, user=request.user)
    army = village.army  # Pobranie obiektu Army powiązanego z wioską

    # Sumowanie wartości jednostek
    current_army = {}
    for unit in army_data.keys():
        inside = getattr(army, f"{unit}_inside", 0)
        outside = getattr(army, f"{unit}_outside", 0)
        current_army[unit] = inside + outside
    print(current_army)
    missing_resources_units = []
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
        army = village.army  # Pobierz obiekt Army powiązany z wioską
        research = village.research

        total_wood_needed = 0
        total_clay_needed = 0
        total_iron_needed = 0

        for unit, costs in army_data.items():
            quantity_key = f'quantity_{unit}'
            quantity = int(request.POST.get(quantity_key, 0))
            if quantity > 0:
                if not getattr(research, unit, False):
                    messages.error(request, f"Jednostka {unit} nie została zbadana.")
                    return redirect('plemiona:barracks_view', village_id=village_id)
                wood_needed = costs['wood'] * quantity
                clay_needed = costs['clay'] * quantity
                iron_needed = costs['iron'] * quantity

                total_wood_needed += wood_needed
                total_clay_needed += clay_needed
                total_iron_needed += iron_needed

        if (village.resources.wood >= total_wood_needed and
            village.resources.clay >= total_clay_needed and
            village.resources.iron >= total_iron_needed):
            for unit, costs in army_data.items():
                quantity_key = f'quantity_{unit}'
                quantity = int(request.POST.get(quantity_key, 0))

                if quantity > 0:
                    # Aktualizacja liczby jednostek w armii
                    unit_inside_field = f'{unit}_inside'
                    current_quantity = getattr(army, unit_inside_field, 0)
                    setattr(army, unit_inside_field, current_quantity + quantity)

            # Aktualizacja surowców w wiosce
            village.resources.wood -= total_wood_needed
            village.resources.clay -= total_clay_needed
            village.resources.iron -= total_iron_needed

            village.resources.save()
            army.save()  # Zapisz zmiany w armii
            village.save()

            # Możesz dodać komunikat o sukcesie rekrutacji
            messages.success(request, 'Units recruited successfully.')
                    # Przekierowanie po pomyślnej rekrutacji
            return redirect('plemiona:barracks_view', village_id=village_id)
        else:
                    # Przekieruj z powrotem do town_hall z komunikatem o braku zasobów
                    missing_resources_units = []
                    if village.resources.wood < total_wood_needed:
                        missing_resources_units.append('drewno')
                    if village.resources.clay < total_clay_needed:
                        missing_resources_units.append('glina')
                    if village.resources.iron < total_iron_needed:
                        missing_resources_units.append('żelazo')

                    if missing_resources_units:
                        request.session['missing_resources_units'] = missing_resources_units
                        return redirect('plemiona:barracks_view', village_id=village_id)


            # Przekierowanie do formularza rekrutacji w przypadku żądania innego niż POST
        return redirect('plemiona:barracks_view', village_id=village_id)


def place_view(request, village_id):
    village = get_object_or_404(Village, id=village_id, user=request.user)
    army = village.army  # Pobranie obiektu Army powiązanego z wioską

    # Sumowanie wartości jednostek
    current_army = {}
    for unit in army_data.keys():
        inside = getattr(army, f"{unit}_inside", 0)
        # outside = getattr(army, f"{unit}_outside", 0)
        current_army[unit] = inside
    # print(current_army)

    missing_units = request.session.pop('missing_units', None)
    messages_units = request.session.pop('messages', None)
    # print(army_data[unit])
    context = {
        'village': village,
        'army_data': army_data,
        'current_army': current_army,  # Dodanie sumowanych wartości do kontekstu
        'missing_units': missing_units,
        'messages_units': messages_units
    }

    return render(request, 'plemiona/place.html', context)




@login_required
def attack_view(request, village_id):
    if request.method == 'POST':
        attacker_village = get_object_or_404(Village, id=village_id)
        attacker_army = attacker_village.army  # Pobierz obiekt Army powiązany z atakującą wioską
        x_coordinate = request.POST.get('coordinate_x')
        y_coordinate = request.POST.get('coordinate_y')
        defender_village = get_object_or_404(Village, coordinate_x=x_coordinate, coordinate_y=y_coordinate)

        # Logika do pobrania jednostek z formularza
        units_to_attack = {}
        total_units_to_attack = 0
        for key in request.POST:
            if key.startswith('quantity-'):
                unit_name = key.split('-')[1]
                quantity = int(request.POST.get(key, 0))
                if quantity > 0:
                    units_to_attack[unit_name] = quantity
                    total_units_to_attack += quantity

        if total_units_to_attack < 15:
            messages.error(request, 'You need to send at least 15 units for an attack.')
            return redirect('plemiona:place_view', village_id=village_id)

        # Sprawdź, czy wystarczająca liczba jednostek jest dostępna wewnątrz wioski
        for unit, quantity in units_to_attack.items():
            if getattr(attacker_army, f"{unit}_inside", 0) < quantity:
                messages.error(request, f'Not enough {unit} in the attacking village.')
                return redirect('plemiona:place_view', village_id=village_id)

            # Odejmij jednostki od armii wewnątrz wioski i dodaj do jednostek poza wioską
            setattr(attacker_army, f"{unit}_inside", getattr(attacker_army, f"{unit}_inside") - quantity)
            setattr(attacker_army, f"{unit}_outside", getattr(attacker_army, f"{unit}_outside", 0) + quantity)
            attacker_army.save()

        # Oblicz czas podróży (funkcja calculate_travel_time musi być zdefiniowana)
        travel_time_seconds = calculate_travel_time(attacker_village, defender_village, units_to_attack)
        print("tworze taska")
        # Zapisz zadanie ataku
        ArmyTask.objects.create(
            attacker_village=attacker_village,
            defender_village=defender_village,
            army_composition=units_to_attack,
            departure_time=timezone.now(),
            arrival_time=timezone.now() + timezone.timedelta(seconds=travel_time_seconds),
            action_type='attack'  # Zaktualizowane zgodnie z nowym modelem
        )

        # Przekieruj z powrotem do widoku wioski z komunikatem o wysłaniu ataku
        messages.success(request, 'Attack has been launched.')
        return redirect('plemiona:place_view', village_id=village_id)

    else:
        # Jeśli metoda nie jest POST, wyświetl formularz ataku
        return render(request, 'attack_form.html', {'village_id': village_id})


from django.db import transaction



def reports_view(request):
    # Retrieve all reports from the database
    reports = Reports.objects.all()
    # Pass the reports to the template
    return render(request, 'plemiona/reports.html', {'reports': reports})
# -------------------------messages_logic------------------------------------------------
def messages_all(request):
    topic_messages_query = Topic_message.objects.filter(Q(sender=request.user) | Q(receiver=request.user)).order_by('-date')

    # Tworzenie słownika zawierającego informacje o wiadomościach i ich statusie odczytu
    topic_messages = {}
    for message in topic_messages_query:
        is_sender = message.sender == request.user
        is_readed = message.is_readed_sender if is_sender else message.is_readed_receiver
        topic_messages[message.id] = {
            'message': message,
            'is_sender': is_sender,
            'is_readed': is_readed
        }

    return render(request, 'plemiona/messages_all.html', {'topic_messages': topic_messages})

def get_message_thread(topic_message):
    # Rozpoczynamy od pierwszej wiadomości w wątku
    thread = [topic_message]

    # Pobieramy wszystkie odpowiedzi (MessageThread) na tę wiadomość
    replies = Answers_Message.objects.filter(topic_message=topic_message).order_by('date')
    for reply in replies:
        thread.append(reply)

    return thread

def message_detail(request, message_id):
    topic_message = get_object_or_404(Topic_message, id=message_id)
    original_message = topic_message

    if request.user == topic_message.sender:
        topic_message.is_readed_sender = True
        print("dobiorca",topic_message.is_readed_sender)
    elif request.user == topic_message.receiver:
        topic_message.is_readed_receiver = True
        print("nadawca",topic_message.is_readed_receiver)

    # Zapisz zmiany w Topic_message
    topic_message.save()
    thread = get_message_thread(topic_message)

    if request.method == 'POST':
        form = MessageThreadForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic_message = topic_message
            reply.replier = request.user
            reply.save()
            if request.user == original_message.sender:
                original_message.is_readed_sender = True
                original_message.is_readed_receiver = False
                print("zmieniam status jako  original_message.sender")
            else:
                original_message.is_readed_sender = False
                original_message.is_readed_receiver = True
                print("zmieniam status jako  reciver")

            original_message.save()
            print("nastapil zapis")
            # Notification.objects.filter(user=request.user, message=topic_message).update(is_read=True)
            return redirect('plemiona:message_detail', message_id=message_id)
    else:
        form = MessageThreadForm()


    return render(request, 'plemiona/message_detail.html', {
        'topic_message': topic_message,
        'thread': thread,
        'form': form
    })


# send message

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Tworzymy nową wiadomość (Topic_message)
            new_topic_message = form.save(commit=False)
            new_topic_message.sender = request.user
            new_topic_message.is_readed_receiver = False  # Ustawienie is_read na False
            new_topic_message.is_readed_sender = True  # Ustawienie is_read na False
            new_topic_message.save()

            # Tworzymy pierwszą odpowiedź w wątku (MessageThread)
            content = form.cleaned_data['content']  # Pobieramy treść z formularza
            new_answers_message = Answers_Message(
                topic_message=new_topic_message,
                replier=request.user,
                content=content
            )
            new_answers_message.save()
            Notification.objects.create(
                user=new_topic_message.receiver,
                message=new_topic_message,
                is_read=False
            )
            # Przekieruj do strony z wysłanymi wiadomościami
            return redirect('plemiona:messages_all')
    else:
        form = MessageForm()

    return render(request, 'plemiona/send_message.html', {'form': form})

from .models import Topic_message, Answers_Message
from .forms import MessageThreadForm


def notifications_view(request):
    user_notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    return render(request, 'plemiona/notifications.html', {'notifications': user_notifications})



#---------------------------------------Views for building without functions--------------------------
def get_building_data(building_name, current_level):
    building_data = buildings_data_dict.get(building_name, {})

    next_levels = []
    for i in range(current_level, current_level + 5):
        level_data = building_data.get(i)
        if level_data:
            next_levels.append({
                'level': i,
                'wood_cost': level_data['wood'],
                'clay_cost': level_data['clay'],
                'iron_cost': level_data['iron'],
                'people_needed': level_data['people_needed'],
                'performance': level_data['performance']
            })
    return next_levels


def sawmill_view(request, village_id):
    village = get_object_or_404(Village, id=village_id)  # Pobierz wioskę
    current_level = village.sawmill  # Pobierz aktualny poziom tartaku z modelu Village
    next_levels = get_building_data('sawmill', current_level)
    return render(request, 'plemiona/buildings_views/sawmill.html', {'next_levels': next_levels, 'village': village})

def clay_pit_view(request, village_id):
    village = get_object_or_404(Village, id=village_id)
    current_level = village.clay_pit
    next_levels = get_building_data('clay_pit', current_level)
    return render(request, 'plemiona/buildings_views/clay_pit.html', {'next_levels': next_levels, 'village': village})

def iron_mine_view(request, village_id):
    village = get_object_or_404(Village, id=village_id)
    current_level = village.iron_mine
    next_levels = get_building_data('iron_mine', current_level)
    return render(request, 'plemiona/buildings_views/iron_mine.html', {'next_levels': next_levels, 'village': village})



def building_requirements(request, village_id):
    village = get_object_or_404(Village, pk=village_id)
    # Assume buildings_lvl_requirements is accessible as a global or passed in some way
    context = {
        'village': village,
        'buildings_requirements': buildings_lvl_requirements,
        # Add more context data as needed
    }
    return render(request, 'plemiona/buildings_views/requirements.html', context)

# calculate can be partly done in front end, backend will anyway calculate it on his side after post request
def forge_view(request, village_id):
    materials = ['wood', 'clay', 'iron']
    village = get_object_or_404(Village, pk=village_id)
    forge_level = getattr(village, 'forge', 0)  # Pobierz poziom kuźni z modelu Village
    forge_performance = buildings_data_dict['forge'][forge_level]['performance']/100  # Pobierz performance dla poziomu kuźni

    # Oblicz czas badania dla każdej jednostki
    research_times = {}
    for unit, data in units.items():
        total_cost = data['wood'] + data['clay'] + data['iron']
        research_time = total_cost * forge_performance  # Możesz dostosować wzór obliczeń
        research_time_converted = convert_seconds_to_time(research_time)
        research_times[unit] = research_time_converted

    print(research_times)
    missing_resources = request.session.pop('missing_resources', None)

    context = {
        'village': village,
        'units': units,
        'research_times': research_times,
        'materials': materials,
        'missing_resources': missing_resources
    }
    return render(request, 'plemiona/buildings_views/forge.html', context)


def start_research(request, village_id, research_type):
    village = get_object_or_404(Village, id=village_id, user=request.user)
    research_data = units[research_type]  # Pobierz dane badania z twojego słownika
    print(research_type)

    tasks_count = ResearchTask.objects.filter(village=village).count()
    if tasks_count >= 2:
        messages.error(request, "za duzo badan w kolejce")
        return redirect('plemiona:forge_view', village_id=village_id)
    # Check if the research has already been completed or is in the queue
    if getattr(village.research, research_type):
        messages.error(request, "Badanie zostało już wykonane.")
        return redirect('plemiona:forge_view', village_id=village_id)

    # Check if the research is already in the queue
    if ResearchTask.objects.filter(village=village, research_type=research_type).exists():
        messages.error(request, "Badanie jest już w kolejce.")
        return redirect('plemiona:forge_view', village_id=village_id)

    for building, required_level in research_data.items():
        if building in ['wood', 'clay', 'iron']:  # Skip resource keys
            continue
        if getattr(village, building, 0) < required_level:
            messages.error(request,
                           f"Nie spełniono wymagań budynku: {building.capitalize()} wymagany poziom {required_level}")
            return redirect('plemiona:forge_view', village_id=village_id)
    # Sprawdź, czy są dostępne zasoby
    if (village.resources.wood >= research_data["wood"] and
            village.resources.clay >= research_data["clay"] and
            village.resources.iron >= research_data["iron"]):

        # Oblicz czas badania
        forge_performance = buildings_data_dict['forge'][village.forge]['performance']
        total_resources_cost = research_data["wood"] + research_data["clay"] + research_data["iron"]
        research_time_seconds = round((total_resources_cost * forge_performance) / 1000)
        last_task = ResearchTask.objects.filter(village=village).order_by('-completion_time').first()
        start_time = last_task.completion_time if last_task else timezone.now()
        completion_time = start_time + timezone.timedelta(seconds=research_time_seconds)
        # Odejmij zasoby
        village.resources.wood -= research_data["wood"]
        village.resources.clay -= research_data["clay"]
        village.resources.iron -= research_data["iron"]
        village.resources.save()

        is_active = tasks_count == 0
        # Zapisanie zadania badawczego w tabeli
        ResearchTask.objects.create(
            village=village,
            research_type=research_type,
            completion_time=completion_time,
            is_active = is_active
        )

        return redirect('plemiona:forge_view', village_id=village_id)

    else:
        print("fiut")
        # Niewystarczające zasoby
        missing_resources = []
        if village.resources.wood < research_data['wood']:
            missing_resources.append('drewno')
        if village.resources.clay < research_data['clay']:
            missing_resources.append('glina')
        if village.resources.iron < research_data['iron']:
            missing_resources.append('żelazo')

        if missing_resources:
            request.session['missing_resources'] = missing_resources
            print(missing_resources,"gejjjjjjjjjjj")
        return redirect('plemiona:forge_view', village_id=village_id)