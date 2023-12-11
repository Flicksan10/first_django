from django import template

from plemiona.buildings_data.buildings import buildings_data_dict

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value, arg):
    """Pobiera atrybut obiektu dynamicznie."""
    return getattr(value, arg, '')

#  ta funkcja powinna być jakos dostosowan do tego co jest  tasks.py
@register.filter(name='calculate_performance')
def calculate_performance(level, building_type):
    building_data = buildings_data_dict.get(building_type, {})
    current_lvl_data = building_data.get(level, {})
    return current_lvl_data.get('performance', 0)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

import math


@register.filter
def floor(value):
    return math.floor(value)