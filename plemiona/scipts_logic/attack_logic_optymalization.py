import cProfile
import random

from line_profiler import profile

from plemiona.army_data import army_data
from plemiona.scipts_logic.attack_logic import simulate_battle


def generate_battle_variations(attacker_units_types, defender_units_types, num_variations=5000):
    variations = []

    for _ in range(num_variations):
        attacker_units = {unit: random.randint(0, 500) for unit in attacker_units_types}
        defender_units = {unit: random.randint(0, 1000) for unit in defender_units_types}

        variations.append({
            "attacker_units": attacker_units,
            "defender_units": defender_units
        })

    return variations

def calculate_specyfic_units():
    attacker_units_types = ["axeman", "light_cavalry", "archer_cavalry", "heavy_cavalry"]
    defender_units_types = ["halberdiers", "pikemen", "archer", "heavy_cavalry"]
    battle_variations = generate_battle_variations(attacker_units_types, defender_units_types)
    return battle_variations


def calculate_performance_50():
    units_variations = calculate_specyfic_units()
    for variation in units_variations:
        attacker_units = variation["attacker_units"]
        defender_units = variation["defender_units"]
        # Wywołaj swoją funkcję z tymi parametrami
        simulate_battle(attacker_units, defender_units, army_data)


from celery import shared_task

@shared_task
def simulate_battle_async(*args, **kwargs):
    return calculate_performance_50()
@profile
def profile_funtion():
    return calculate_performance_50

# cProfile.run('calculate_performance_50()')