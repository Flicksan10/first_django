from plemiona.army_data import army_data
import random


# obliczenie ataku i stosunku sił(infrantry,cavalry,archer) jednostek, które atakują
def calculate_attack_distribution(attacker_units, army_data):
    total_attack = sum(count * army_data[unit]["attack"] for unit, count in attacker_units.items())
    attack_distribution = {}

    for unit, count in attacker_units.items():
        if count > 0:
            unit_attack = count * army_data[unit]["attack"]
            attack_type = army_data[unit]["attack_type"]

            if attack_type not in attack_distribution:
                attack_distribution[attack_type] = {
                    "total_units": 0,
                    "total_attack": 0,
                    "percentage": 0,
                    "units": {}
                }

            attack_distribution[attack_type]["total_units"] += count
            attack_distribution[attack_type]["total_attack"] += unit_attack
            attack_distribution[attack_type]["units"][unit] = count

    for attack_type in attack_distribution:
        attack_distribution[attack_type]["percentage"] = (attack_distribution[attack_type]["total_attack"] / total_attack) * 100
    print(attack_distribution)
    return attack_distribution

# opytmalizacja jednostek, które będa sie bronic, ten algorytm jest do poprawy bo dziala strasznie dziwnie
def optimize_defense_distribution(defender_units, attack_distribution, army_data, iterations=10000):
    best_defense_distribution = None
    best_defense_score = -1

    for _ in range(iterations):
        current_defense_distribution = distribute_defense_based_on_attack(defender_units, attack_distribution, army_data)
        current_defense_score = calculate_defense_score(current_defense_distribution, attack_distribution, army_data)

        if current_defense_score > best_defense_score:
            best_defense_distribution = current_defense_distribution
            best_defense_score = current_defense_score
    print(best_defense_distribution)
    return best_defense_distribution


def distribute_defense_based_on_attack(defender_units, attack_distribution, army_data):
    defense_distribution = {
        "infantry": {"total_units": 0, "total_defense": 0, "units": {}},
        "cavalry": {"total_units": 0, "total_defense": 0, "units": {}},
        "archer": {"total_units": 0, "total_defense": 0, "units": {}}
    }

    remaining_units = defender_units.copy()

    for defense_type in ["infantry", "cavalry", "archer"]:
        if defense_type in attack_distribution:
            required_units = int(attack_distribution[defense_type]["percentage"] / 100 * sum(defender_units.values()))
            for unit, count in sorted(remaining_units.items(), key=lambda x: -army_data[x[0]][f"defense_{defense_type}"]):
                if count > 0:
                    allocated_units = min(count, required_units)
                    defense_distribution[defense_type]["units"][unit] = allocated_units
                    defense_distribution[defense_type]["total_units"] += allocated_units
                    defense_distribution[defense_type]["total_defense"] += allocated_units * army_data[unit][f"defense_{defense_type}"]
                    remaining_units[unit] -= allocated_units
                    required_units -= allocated_units

    # Rozdziel pozostałe jednostki losowo
    for unit, count in remaining_units.items():
        if count > 0:
            for _ in range(count):
                defense_type = random.choice(["infantry", "cavalry", "archer"])
                defense_distribution[defense_type]["units"].setdefault(unit, 0)
                defense_distribution[defense_type]["units"][unit] += 1
                defense_distribution[defense_type]["total_units"] += 1
                defense_distribution[defense_type]["total_defense"] += army_data[unit][f"defense_{defense_type}"]

    return defense_distribution

def calculate_defense_score(defense_distribution, attack_distribution, army_data):
    score = 0
    for defense_type in defense_distribution:
        score += defense_distribution[defense_type]["total_defense"] * (attack_distribution.get(defense_type, {}).get("percentage", 0) / 100)
    return score


def calculate_battle_outcome(attack_distribution, defense_distribution):
    battle_outcome = {}

    for category in ["infantry", "cavalry", "archer"]:
        attacker_power = attack_distribution[category]['total_attack']
        defender_power = defense_distribution[category]['total_defense']

        if attacker_power > defender_power:
            winner = 'attacker'
            loser_power = defender_power
        else:
            winner = 'defender'
            loser_power = attacker_power

        loss_ratio = loser_power / max(attacker_power, defender_power)
        loss_ratio_adjusted = loss_ratio - random.uniform(0.05, 0.1)

        battle_outcome[category] = {
            'winner': winner,
            'loser_loss_percentage': 100,
            'winner_loss_percentage': max(0, loss_ratio_adjusted * 100)
        }
    print(battle_outcome)
    return battle_outcome


def apply_battle_results(attack_distribution, defense_distribution, battle_outcome):
    for category in ["infantry", "cavalry", "archer"]:
        outcome = battle_outcome[category]
        winner = outcome['winner']
        winner_loss_percentage = outcome['winner_loss_percentage']
        loser_loss_percentage = outcome['loser_loss_percentage']

        if winner == 'attacker':
            # Redukcja jednostek obrońcy do 0
            defense_distribution[category]['units'] = {unit: 0 for unit in defense_distribution[category]['units']}
            # Redukcja jednostek atakującego
            for unit, count in attack_distribution[category]['units'].items():
                attack_distribution[category]['units'][unit] = int(count * (1 - winner_loss_percentage / 100))
        else:
            # Redukcja jednostek atakującego do 0
            attack_distribution[category]['units'] = {unit: 0 for unit in attack_distribution[category]['units']}
            # Redukcja jednostek obrońcy
            for unit, count in defense_distribution[category]['units'].items():
                defense_distribution[category]['units'][unit] = int(count * (1 - winner_loss_percentage / 100))

    return attack_distribution, defense_distribution



# Przykładowe dane armii

attacker_units = {"axeman": 1000,"light_cavalry": 300,"archer_cavalry":100}
defender_units = {'archer': 1000,"pikemen": 1000,'halberdiers':300}
# Obliczanie dystrybucji ataku
attack_distribution = calculate_attack_distribution(attacker_units, army_data)
# # Rozdzielenie obrony według preferencji
defense_distribution = optimize_defense_distribution(defender_units, attack_distribution, army_data)
# # Tutaj możesz zaimplementować logikę starcia na podstawie obliczonych dystrybucji
battle_outcome = calculate_battle_outcome(attack_distribution, defense_distribution)
attack_result,defense_result = apply_battle_results(attack_distribution, defense_distribution, battle_outcome)
print(attack_result)
print(defense_result)
# print(defense_result)
# print(defense_result)

# ({'cavalry': {'total_units': 300, 'total_attack': 39000, 'percentage': 42.857142857142854, 'units': {'light_cavalry': 25}},
#   'infantry': {'total_units': 1000, 'total_attack': 40000, 'percentage': 43.956043956043956, 'units': {'axeman': 0}},
#   'archer': {'total_units': 100, 'total_attack': 12000, 'percentage': 13.186813186813188, 'units': {'archer_cavalry': 76}}},
#  {'infantry': {'total_units': 880, 'total_defense': 44000, 'units': {'archer': 145, 'pikemen': 0}},
# 'cavalry': {'total_units': 857, 'total_defense': 38565, 'units': {'pikemen': 0, 'archer': 0}},
# 'archer': {'total_units': 263, 'total_defense': 3460, 'units': {'pikemen': 0, 'archer': 0}}})
