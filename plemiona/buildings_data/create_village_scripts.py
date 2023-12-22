from django.db import transaction

from plemiona.buildings_data.buildings import buildings_data_dict
from plemiona.models import BuildingProperties, Village


def initialize_building_properties_new_village(village):
    with transaction.atomic():
        for building_type in buildings_data_dict.keys():
            level_field_name = building_type
            if hasattr(village, level_field_name):
                current_level = getattr(village, level_field_name)

                BuildingProperties.objects.update_or_create(
                    village=village,
                    building_type=building_type,
                    defaults={
                        'level': current_level,
                        'performance': calculate_performance_building(building_type, current_level),
                        'bonus': 0
                    }
                )

def calculate_performance_building(building_type, level):
    # Pobierz podstawową wydajność z buildings_data_dict
    base_performance = buildings_data_dict[building_type][level]['performance']
    return base_performance

