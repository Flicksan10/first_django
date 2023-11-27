from plemiona.army_data import army_data



def calculate_combat_points(unit_counts, army_data, attack=True):
    points = {"infantry": 0, "cavalry": 0, "archer": 0}
    for unit, count in unit_counts.items():
        if count > 0:
            unit_type = army_data[unit]["type"]
            if attack:
                points[unit_type] += count * army_data[unit]["attack"]
            else:
                points[unit_type] += count * army_data[unit]["infantry_defense"]
                # Możesz dodać logikę dla obrony przeciwko kawalerii i łucznikom
    return points

def attack_logic_function(attacker_village, defender_village, request, village_id):
    # Pobierz liczbę jednostek dla atakującego i obrońcy
    attacker_units = {unit: int(request.POST.get(f'quantity_{unit}', 0)) for unit, _ in army_data.items()}
    defender_units = {unit: getattr(defender_village, unit, 0) for unit, _ in army_data.items()}

    # Oblicz punkty ataku i obrony
    attacker_points = calculate_combat_points(attacker_units, army_data, attack=True)
    defender_points = calculate_combat_points(defender_units, army_data, attack=False)

    # Logika walki dla każdego etapu
    def compare_points(attacker, defender):
        result = {"infantry": 0, "cavalry": 0, "archer": 0}
        for key in result.keys():
            result[key] = attacker[key] - defender[key]
        return result

    # Porównaj punkty w każdym etapie walki
    combat_results = compare_points(attacker_points, defender_points)

    # Oblicz ogólny wynik
    total_attacker_points = sum(attacker_points.values())
    total_defender_points = sum(defender_points.values())
    overall_result = total_attacker_points - total_defender_points

    # Możesz tutaj dodać logikę do określenia zwycięzcy
    if overall_result > 0:
        print(f"Atakujacy wygrywa z przewaga {overall_result} punktow.")
    elif overall_result < 0:
        print(f"Obronca wygrywa z przewaga {overall_result} punktow.")
    else:
        print("Bitwa zakonczyla sie remisem.")

    # Wyniki dla każdego etapu
    print("Wyniki dla poszczegolnych etapow walki:")
    for key, value in combat_results.items():
        if value > 0:
            print(f"Atakujacy wygrywa w kategorii {key} z przewaga {value} punktow.")
        elif value < 0:
            print(f"Obronca wygrywa w kategorii {key} z przewaga {-value} punktow.")
        else:
            print(f"Remis w kategorii {key}.")

    # Zwróć wyniki dla dalszej analizy lub użycia
    print(overall_result,combat_results)
    return overall_result, combat_results



def attack_logic_function(attacker_village, defender_village, request, village_id):
    # Pobierz liczbę jednostek dla atakującego i obrońcy
    attacker_units = {unit: int(request.POST.get(f'quantity_{unit}', 0)) for unit, _ in army_data.items()}
    defender_units = {unit: getattr(defender_village, unit, 0) for unit, _ in army_data.items()}

    # Oblicz punkty ataku i obrony dla każdego typu jednostki
    attacker_points = {
        "infantry": calculate_combat_points(attacker_units, army_data, "infantry", attack=True),
        "cavalry": calculate_combat_points(attacker_units, army_data, "cavalry", attack=True),
        "archer": calculate_combat_points(attacker_units, army_data, "archer", attack=True)
    }
    defender_points = {
        "infantry": calculate_combat_points(defender_units, army_data, "infantry", attack=False),
        "cavalry": calculate_combat_points(defender_units, army_data, "cavalry", attack=False),
        "archer": calculate_combat_points(defender_units, army_data, "archer", attack=False)
    }

    # Logika porównywania punktów
    def compare_points(attacker, defender):
        result = {"infantry": 0, "cavalry": 0, "archer": 0}
        for key in result.keys():
            result[key] = attacker[key] - defender[key]
        return result

    # Porównaj punkty w każdym etapie walki
    combat_results = compare_points(attacker_points, defender_points)

    # Oblicz ogólny wynik
    overall_result = sum(combat_results.values())

    # Logika wyświetlania wyników
    # Możesz tutaj dodać logikę do określenia zwycięzcy
    if overall_result > 0:
        print(f"Atakujacy wygrywa z przewaga {overall_result} punktow.")
    elif overall_result < 0:
        print(f"Obronca wygrywa z przewaga {overall_result} punktow.")
    else:
        print("Bitwa zakonczyla sie remisem.")

    # Wyniki dla każdego etapu
    print("Wyniki dla poszczegolnych etapow walki:")
    for key, value in combat_results.items():
        if value > 0:
            print(f"Atakujacy wygrywa w kategorii {key} z przewaga {value} punktow.")
        elif value < 0:
            print(f"Obronca wygrywa w kategorii {key} z przewaga {-value} punktow.")
        else:
            print(f"Remis w kategorii {key}.")

    # Zwróć wyniki dla dalszej analizy lub użycia
    print(overall_result, combat_results)

    return overall_result, combat_results