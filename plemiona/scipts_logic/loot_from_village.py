def calculate_loot(battle_result, army_data, defender_village):
    total_payload = sum(battle_result[unit] * army_data[unit]["payload"] for unit in battle_result)

    available_resources = {
        "wood": defender_village.resources.wood,
        "clay": defender_village.resources.clay,
        "iron": defender_village.resources.iron
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

    # Aktualizuj stan surowców w atakowanej wiosce
    defender_village.resources.wood -= looted_resources["wood"]
    defender_village.resources.clay -= looted_resources["clay"]
    defender_village.resources.iron -= looted_resources["iron"]
    defender_village.resources.save()

    return looted_resources
