from plemiona.army_data import army_data
from plemiona.models import ArmyTask
from django.utils import timezone

def create_return_task(attacker_village, defender_village, surviving_units, looted_resources):
    # Oblicz czas podróży powrotnej
    travel_time_seconds = calculate_travel_time(attacker_village, defender_village, surviving_units)

    # Utwórz zadanie powrotu
    ArmyTask.objects.create(
        attacker_village=attacker_village,
        defender_village=defender_village,
        army_composition=surviving_units,
        departure_time=timezone.now(),
        arrival_time=timezone.now() + timezone.timedelta(seconds=travel_time_seconds),
        looted_resources=looted_resources,
        action_type='return_attack'
    )

def calculate_travel_time(attacker_village, defender_village, army):
    # Oblicz odległość między wioskami
    distance = ((defender_village.coordinate_x - attacker_village.coordinate_x) ** 2 +
                (defender_village.coordinate_y - attacker_village.coordinate_y) ** 2) ** 0.5
    print(attacker_village.coordinate_x, attacker_village.coordinate_y)
    print(defender_village.coordinate_x, defender_village.coordinate_y)
    print(distance)

    # Znajdź najwolniejszą jednostkę w armii
    slowest_speed = min(army_data[unit]['speed'] for unit in army if army[unit] > 0)

    # Oblicz czas podróży (przykładowa formuła, może wymagać dostosowania)
    travel_time_seconds = distance * slowest_speed * 0.8  # Przykładowa konwersja na sekundy
    print(travel_time_seconds)
    return travel_time_seconds
