from celery import shared_task

from djangoProject1.celery import app
from .buildings_data.buildings import buildings_data_dict
# from .buildings_data import buildings
from .models import Village

# @shared_task
@app.task
def update_resources():
    print("dziam")
    villages = Village.objects.all()
    for village in villages:
        # Zakładając, że masz funkcję do pobierania wydajności na podstawie poziomu
        wood_increase = get_performance(village.sawmill, 'sawmill',buildings_data_dict['sawmill'])
        clay_increase = get_performance(village.clay_pit, 'clay_pit',buildings_data_dict['clay_pit'])
        iron_increase = get_performance(village.iron_mine, 'iron_mine',buildings_data_dict['iron_mine'])

        village.wood += wood_increase
        village.clay += clay_increase
        village.iron += iron_increase
        # village.wood += 50000
        # village.clay += 50000
        # village.iron += 50000
        # print(village.wood)
        village.save()

def get_performance(level, building_type, resource_data):
    # level -= 1  # Dostosowanie poziomu indeksowanie rozpoczyna się od 0

    if building_type == 'sawmill':
        print(resource_data[level]["performance"])
        data = resource_data[level]["performance"] / 6
    elif building_type == 'clay_pit':
        data = resource_data[level]["performance"] / 6
    elif building_type == 'iron_mine':
        data = resource_data[level]["performance"] / 6
    else:
        raise ValueError("Nieznany typ budynku")

    return data
