# from plemiona.army_data import army_data
#
#
# def calculate_unit_potential(units, army_data):
#     unit_potentials = {}
#     for unit, count in units.items():
#         if count > 0:
#             unit_potentials[unit] = {
#                 "quantity": count,
#                 "attack": count * army_data[unit]["attack"],
#                 "defense_infantry": count * army_data[unit]["defense_infantry"],
#                 "defense_cavalry": count * army_data[unit]["defense_cavalry"],
#                 "defense_archer": count * army_data[unit]["defense_archer"],
#                 "type":army_data[unit]["type"]
#             }
#     return unit_potentials
#
# # Przykładowe dane armii atakującej/broniącej
# attacker_units = {"pikemen": 10, "axeman": 5,"light_cavalry":2}
# defender_units = {"pikemen": 15, "axeman": 3}
#
# # Obliczanie potencjału bojowego
# attacker_potential = calculate_unit_potential(attacker_units, army_data)
# defender_potential = calculate_unit_potential(defender_units, army_data)
#
# print("Potencjał bojowy atakującego:", attacker_potential)
# print("Potencjał bojowy obrońcy:", defender_potential)
#
# def compare_combat_potential(attacker_potential, defender_potential, army_data):
#     combat_results = {
#         "infantry": {"attacker": 0, "defender": 0},
#         "archer": {"attacker": 0, "defender": 0},
#         "cavalry": {"attacker": 0, "defender": 0}
#     }
#
#     for unit, data in attacker_potential.items():
#         unit_type = army_data[unit]["type"]
#         combat_results[unit_type]["attacker"] += data["attack"]
#
#     for unit, data in defender_potential.items():
#         unit_type = army_data[unit]["type"]
#         combat_results[unit_type]["defender"] += data[f"defense_{unit_type}"]
#     print(combat_results)
#     return combat_results
#
# compare_combat_potential(attacker_potential,defender_potential,army_data)
from plemiona.army_data import army_data


# def calculate_attack_distribution(attacker_units, army_data):
#     total_attack = sum(count * army_data[unit]["attack"] for unit, count in attacker_units.items())
#     attack_distribution = {}
#
#     for unit, count in attacker_units.items():
#         unit_attack = count * army_data[unit]["attack"]
#         attack_type = army_data[unit]["attack_type"]
#         attack_distribution[attack_type] = attack_distribution.get(attack_type, 0) + unit_attack
#
#     for attack_type in attack_distribution:
#         attack_distribution[attack_type] = (attack_distribution[attack_type] / total_attack) * 100
#
#     return attack_distribution

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

    return attack_distribution

# def distribute_defense_according_to_preference(defender_units, attack_distribution, army_data):
#     defense_distribution = {"infantry": [], "cavalry": [], "archer": []}
#     remaining_units = defender_units.copy()
#
#     for defense_type in ["cavalry", "infantry", "archer"]:
#         required_percentage = attack_distribution.get(defense_type, 0)
#         for unit, count in remaining_units.items():
#             if count > 0 and army_data[unit]["defense_preference"][0] == defense_type:
#                 defense_distribution[defense_type].append((unit, count))
#                 remaining_units[unit] = 0
#
#     # Rozdziel pozostałe jednostki według kolejnych preferencji
#     for unit, count in remaining_units.items():
#         if count > 0:
#             for preference in army_data[unit]["defense_preference"]:
#                 if preference in defense_distribution:
#                     defense_distribution[preference].append((unit, count))
#                     break
#
#     return defense_distribution

# def distribute_defense_according_to_preference(defender_units, attack_distribution, army_data):
#     defense_distribution = {
#         "infantry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "cavalry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "archer": {"total_units": 0, "total_defense": 0, "units": {}}
#     }
#
#     # Sortuj jednostki obronne według ich preferencji obrony
#     sorted_defense_units = sorted(defender_units.items(), key=lambda x: army_data[x[0]]["defense_preference"])
#
#     # Przydziel jednostki do kategorii obrony na podstawie attack_distribution
#     for unit, count in sorted_defense_units:
#         for preference in army_data[unit]["defense_preference"]:
#             defense_type = ["infantry", "cavalry", "archer"][preference - 1]
#             if attack_distribution.get(defense_type, {}).get("percentage", 0) > 0:
#                 defense_points = count * army_data[unit][f"defense_{defense_type}"]
#                 defense_distribution[defense_type]["units"][unit] = count
#                 defense_distribution[defense_type]["total_units"] += count
#                 defense_distribution[defense_type]["total_defense"] += defense_points
#                 # Zmniejsz zapotrzebowanie na ten typ obrony
#                 attack_distribution[defense_type]["percentage"] -= (count / sum(defender_units.values())) * 100
#                 break
#
#     return defense_distribution
# def distribute_defense_according_to_preference(defender_units, attack_distribution, army_data):
#     defense_distribution = {
#         "infantry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "cavalry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "archer": {"total_units": 0, "total_defense": 0, "units": {}}
#     }
#
#     total_defender_units = sum(defender_units.values())
#
#     # Mapowanie typów obrony do numerów preferencji
#     defense_type_to_preference = {"infantry": 1, "cavalry": 2, "archer": 3}
#
#     # Przydziel jednostki do kategorii obrony na podstawie attack_distribution
#     for defense_type in ["infantry", "cavalry", "archer"]:
#         required_units = round((attack_distribution.get(defense_type, {}).get("percentage", 0) / 100) * total_defender_units)
#         for unit, count in sorted(defender_units.items(), key=lambda x: army_data[x[0]]["defense_preference"].index(defense_type_to_preference[defense_type])):
#             if required_units <= 0:
#                 break
#             if count > 0:
#                 units_to_assign = min(count, required_units)
#                 defense_points = units_to_assign * army_data[unit][f"defense_{defense_type}"]
#                 defense_distribution[defense_type]["units"][unit] = units_to_assign
#                 defense_distribution[defense_type]["total_units"] += units_to_assign
#                 defense_distribution[defense_type]["total_defense"] += defense_points
#                 defender_units[unit] -= units_to_assign
#                 required_units -= units_to_assign
#
#     return defense_distribution

#  jeden z najlepszych !!
# def distribute_defense_according_to_preference(defender_units, attack_distribution, army_data):
#     defense_distribution = {
#         "infantry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "cavalry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "archer": {"total_units": 0, "total_defense": 0, "units": {}}
#     }
#
#     total_defender_units = sum(defender_units.values())
#
#     # Mapowanie typów obrony do numerów preferencji
#     defense_type_to_preference = {"infantry": 1, "cavalry": 2, "archer": 3}
#
#     # Przydziel jednostki do kategorii obrony na podstawie attack_distribution
#     for defense_type in ["infantry", "cavalry", "archer"]:
#         required_units = round((attack_distribution.get(defense_type, {}).get("percentage", 0) / 100) * total_defender_units)
#         sorted_units = sorted(defender_units.items(), key=lambda x: army_data[x[0]]["defense_preference"].index(defense_type_to_preference[defense_type]))
#
#         for unit, count in sorted_units:
#             if required_units <= 0 or count == 0:
#                 continue
#
#             units_to_assign = min(count, required_units)
#             defense_points = units_to_assign * army_data[unit][f"defense_{defense_type}"]
#             defense_distribution[defense_type]["units"][unit] = units_to_assign
#             defense_distribution[defense_type]["total_units"] += units_to_assign
#             defense_distribution[defense_type]["total_defense"] += defense_points
#             defender_units[unit] -= units_to_assign
#             required_units -= units_to_assign
#
#             # Jeśli jednostka ma więcej niż jedną preferencję, rozważ jej ponowne przydzielenie
#             if len(army_data[unit]["defense_preference"]) > 1 and defender_units[unit] > 0:
#                 next_preference = army_data[unit]["defense_preference"][1]
#                 next_defense_type = list(defense_type_to_preference.keys())[list(defense_type_to_preference.values()).index(next_preference)]
#                 if next_defense_type != defense_type:
#                     sorted_units.append((unit, defender_units[unit]))
#                     sorted_units.sort(key=lambda x: army_data[x[0]]["defense_preference"].index(next_preference))
#
#     return defense_distribution

# def optimize_defense_distribution(defender_units, attack_distribution, army_data):
#     defense_distribution = {
#         "infantry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "cavalry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "archer": {"total_units": 0, "total_defense": 0, "units": {}}
#     }
#
#     total_defender_units = sum(defender_units.values())
#
#     # Przydziel jednostki do kategorii obrony na podstawie ich efektywności
#     for defense_type in ["infantry", "cavalry", "archer"]:
#         required_units = round((attack_distribution.get(defense_type, {}).get("percentage", 0) / 100) * total_defender_units)
#
#         # Sortuj jednostki według ich efektywności obronnej w danej kategorii
#         sorted_units = sorted(defender_units.items(), key=lambda x: -army_data[x[0]][f"defense_{defense_type}"])
#
#         for unit, count in sorted_units:
#             if required_units <= 0 or count == 0:
#                 continue
#
#             units_to_assign = min(count, required_units)
#             defense_points = units_to_assign * army_data[unit][f"defense_{defense_type}"]
#             defense_distribution[defense_type]["units"][unit] = units_to_assign
#             defense_distribution[defense_type]["total_units"] += units_to_assign
#             defense_distribution[defense_type]["total_defense"] += defense_points
#             defender_units[unit] -= units_to_assign
#             required_units -= units_to_assign
#
#     return defense_distribution

# def optimize_defense_distribution_v2(defender_units, attack_distribution, army_data):
#     defense_distribution = {
#         "infantry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "cavalry": {"total_units": 0, "total_defense": 0, "units": {}},
#         "archer": {"total_units": 0, "total_defense": 0, "units": {}}
#     }
#
#     total_defender_units = sum(defender_units.values())
#
#     # Przydziel jednostki do kategorii obrony na podstawie procentowego udziału ataku
#     for defense_type in ["infantry", "cavalry", "archer"]:
#         required_units = round((attack_distribution.get(defense_type, {}).get("percentage", 0) / 100) * total_defender_units)
#
#         # Sortuj jednostki według ich efektywności obronnej w danej kategorii
#         sorted_units = sorted(defender_units.items(), key=lambda x: -army_data[x[0]][f"defense_{defense_type}"])
#
#         for unit, count in sorted_units:
#             if required_units <= 0 or count == 0:
#                 continue
#
#             units_to_assign = min(count, required_units)
#             defense_points = units_to_assign * army_data[unit][f"defense_{defense_type}"]
#             defense_distribution[defense_type]["units"][unit] = units_to_assign
#             defense_distribution[defense_type]["total_units"] += units_to_assign
#             defense_distribution[defense_type]["total_defense"] += defense_points
#             defender_units[unit] -= units_to_assign
#             required_units -= units_to_assign
#
#     # Rozdziel pozostałe jednostki według ich drugiej preferencji
#     for unit, count in defender_units.items():
#         if count > 0:
#             for preference in army_data[unit]["defense_preference"]:
#                 defense_type = ["infantry", "cavalry", "archer"][preference - 1]
#                 defense_points = count * army_data[unit][f"defense_{defense_type}"]
#                 defense_distribution[defense_type]["units"][unit] = count
#                 defense_distribution[defense_type]["total_units"] += count
#                 defense_distribution[defense_type]["total_defense"] += defense_points
#                 break
#
#     return defense_distribution
import random

def optimize_defense_distribution(defender_units, attack_distribution, army_data, iterations=10000):
    best_defense_distribution = None
    best_defense_score = -1

    for _ in range(iterations):
        current_defense_distribution = distribute_defense_based_on_attack(defender_units, attack_distribution, army_data)
        current_defense_score = calculate_defense_score(current_defense_distribution, attack_distribution, army_data)

        if current_defense_score > best_defense_score:
            best_defense_distribution = current_defense_distribution
            best_defense_score = current_defense_score

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

# Przykładowe wywołanie
# optimized_defense = optimize_defense_distribution(defender_units, attack_distribution, army_data)


# Przykładowe dane armii
# attacker_units = {"light_cavalry": 100, "axeman": 20,"archer_cavalry":10}
# defender_units = {'archer':28,"pikemen": 25, "halberdiers": 25,"heavy_cavalry":10}
attacker_units = {"light_cavalry": 300,"axeman": 1000,"archer_cavalry":100}
defender_units = {'archer': 1000,"pikemen": 1000}
# Obliczanie dystrybucji ataku
attack_distribution = calculate_attack_distribution(attacker_units, army_data)
print(attack_distribution)
# # Rozdzielenie obrony według preferencji
defense_distribution = optimize_defense_distribution(defender_units, attack_distribution, army_data)
print(defense_distribution)
# # Tutaj możesz zaimplementować logikę starcia na podstawie obliczonych dystrybucji



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

    return battle_outcome


battle_outcome = calculate_battle_outcome(attack_distribution, defense_distribution)
print(battle_outcome)


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


wynik=apply_battle_results(attack_distribution, defense_distribution, battle_outcome)

print(wynik)

({'cavalry': {'total_units': 300, 'total_attack': 39000, 'percentage': 42.857142857142854, 'units': {'light_cavalry': 25}},
  'infantry': {'total_units': 1000, 'total_attack': 40000, 'percentage': 43.956043956043956, 'units': {'axeman': 0}},
  'archer': {'total_units': 100, 'total_attack': 12000, 'percentage': 13.186813186813188, 'units': {'archer_cavalry': 76}}},
 {'infantry': {'total_units': 880, 'total_defense': 44000, 'units': {'archer': 145, 'pikemen': 0}},
'cavalry': {'total_units': 857, 'total_defense': 38565, 'units': {'pikemen': 0, 'archer': 0}},
'archer': {'total_units': 263, 'total_defense': 3460, 'units': {'pikemen': 0, 'archer': 0}}})


