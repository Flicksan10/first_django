import logging

from django.db import transaction

from plemiona.army_data import army_data
from plemiona.models import Village, Reports, ArmyTask
from plemiona.scipts_logic.after_battle_return import create_return_task
from plemiona.scipts_logic.loot_from_village import calculate_loot


def update_units_after_battle(attacker_village_id, defender_village_id, units_to_attack, defender_units, winner,
                              battle_result):
    # Pobierz wioski
    attacker_village = Village.objects.get(id=attacker_village_id)
    defender_village = Village.objects.get(id=defender_village_id)

    if winner == 'attacker':
        # Atakujący wygrywa
        for unit, count in units_to_attack.items():
            loss = count - battle_result.get(unit, 0)
            current_count = getattr(attacker_village.army, f"{unit}_outside", 0)
            setattr(attacker_village.army, f"{unit}_outside", max(current_count - loss, 0))

        for unit, count in defender_units.items():
            current_count = getattr(defender_village.army, f"{unit}_inside", 0)
            setattr(defender_village.army, f"{unit}_inside", max(current_count - count, 0))
        loot = calculate_loot(battle_result, army_data, defender_village)
        create_return_task(attacker_village, defender_village, battle_result, loot)

        print("zebrano tyle", loot)
    else:
        loot: {}
        # Obrońca wygrywa
        for unit, count in units_to_attack.items():
            current_count = getattr(attacker_village.army, f"{unit}_outside", 0)
            setattr(attacker_village.army, f"{unit}_outside", max(current_count - count, 0))

        for unit, count in defender_units.items():
            loss = count - battle_result.get(unit, 0)
            current_count = getattr(defender_village.army, f"{unit}_inside", 0)
            setattr(defender_village.army, f"{unit}_inside", max(current_count - loss, 0))

    save_battle_report(attacker_village.id, defender_village.id, units_to_attack, defender_units, winner, battle_result,
                       loot)

    # Zapisz zmiany w bazie danych
    attacker_village.army.save()
    defender_village.army.save()


def save_battle_report(attacker_village_id, defender_village_id, units_to_attack, defender_units, winner,
                       battle_result, loot):
    # Retrieve the village instances
    attacker_village = Village.objects.get(id=attacker_village_id)
    defender_village = Village.objects.get(id=defender_village_id)

    # Determine the winner and loser
    if winner == 'attacker':
        winner_user = attacker_village.user
        loser_user = defender_village.user
    else:
        winner_user = defender_village.user
        loser_user = attacker_village.user
    logging.warning('Watch outs!')
    # Create a new Reports instance
    report = Reports(
        attacker_user=attacker_village.user,
        defender_user=defender_village.user,
        village_attacker=attacker_village,
        village_defender=defender_village,
        attacker_army=units_to_attack,
        defender_army=defender_units,
        result=battle_result,
        winner=winner_user,
        loser=loser_user,
        loot=loot
    )

    # Save the Reports instance
    report.save()

    return report
