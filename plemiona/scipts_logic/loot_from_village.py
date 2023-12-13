def calculate_loot(battle_result, army_data, defender_village,attacker_village):
    total_payload = sum(battle_result[unit] * army_data[unit]["payload"] for unit in battle_result)

    available_resources = {
        "wood": defender_village.wood,
        "clay": defender_village.clay,
        "iron": defender_village.iron
    }

    total_resources = sum(available_resources.values())
    looted_resources = {"wood": 0, "clay": 0, "iron": 0}

    if total_resources == 0:
        return looted_resources  # Brak surowców do zabrania

    for resource in available_resources:
        # Proporcjonalny podział surowców
        proportion = available_resources[resource] / total_resources
        looted_amount = min(int(total_payload * proportion), available_resources[resource])
        looted_resources[resource] += looted_amount
        available_resources[resource] -= looted_amount
    print(looted_resources)
    # dodać with transaction.atomic(): gdyby nie była wywołana w innej funkcji np update_units_after_battle
    # Aktualizuj stan surowców w atakowanej wiosce
    defender_village.resources.wood -= looted_resources["wood"]
    defender_village.resources.clay -= looted_resources["clay"]
    defender_village.resources.iron -= looted_resources["iron"]
    defender_village.resources.save()
    attacker_village.resources.wood += looted_resources["wood"]
    attacker_village.resources.clay += looted_resources["clay"]
    attacker_village.resources.iron += looted_resources["iron"]
    attacker_village.resources.save()


    return looted_resources
