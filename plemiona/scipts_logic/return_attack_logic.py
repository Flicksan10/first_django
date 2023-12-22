def handle_return_attack(task):
    attacker_village = task.attacker_village
    attacker_army = attacker_village.army
    looted_resources = task.looted_resources
    surviving_units = task.army_composition

    # Dodaj przetrwałe jednostki do armii wewnątrz wioski
    for unit, quantity in surviving_units.items():
        current_quantity_inside = getattr(attacker_army, f"{unit}_inside", 0)
        current_quantity_outside = getattr(attacker_army, f"{unit}_outside", 0)
        setattr(attacker_army, f"{unit}_inside", current_quantity_inside + quantity)
        setattr(attacker_army, f"{unit}_outside", current_quantity_outside - quantity)

    # Dodaj zdobyte surowce do zasobów wioski
    attacker_village.resources.wood += looted_resources.get('wood', 0)
    attacker_village.resources.clay += looted_resources.get('clay', 0)
    attacker_village.resources.iron += looted_resources.get('iron', 0)

    # Zapisz zmiany
    attacker_army.save()
    attacker_village.resources.save()

    # Usuń wykonane zadanie
    task.delete()