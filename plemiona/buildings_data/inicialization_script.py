from django.db import transaction

from plemiona.buildings_data.buildings import buildings_data_dict
from plemiona.models import Village, BuildingProperties


def initialize_building_properties():
    with transaction.atomic():
        print("chuj")
        for village in Village.objects.all():
            for building_type in buildings_data_dict.keys():
                print(building_type)
                level_field_name = building_type
                if hasattr(village, level_field_name):
                    current_level = getattr(village, level_field_name)

                    BuildingProperties.objects.update_or_create(
                        village=village,
                        building_type=building_type,
                        defaults={
                            'level': current_level,
                            'performance': calculate_performance(building_type, current_level),
                            'bonus': 0
                        }
                    )



def calculate_performance(building_type, level):
    # Pobierz podstawową pojemność z buildings_data_dict i zastosuj bonusy
    base_capacity = buildings_data_dict[building_type][level]['performance']
    # bonus_factor = get_bonus_factor()  # funkcja do obliczania bonusów
    # return base_capacity * (1 + bonus_factor)
    return base_capacity