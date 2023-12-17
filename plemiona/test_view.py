def reports_view(request):
    # Retrieve all reports from the database
    reports = Reports.objects.all()
    #
    # units_to_attack = {"light_cavalry": 100}
    # defender_units = {}
    # departure_time = "2023-12-17 17:12:14.954351"
    # arrival_time = "2023-12-17 17:22:14.954356"
    # attacker_village_id = 5
    # defender_village_id = 22
    # action_type = "attack"
    # winner = 'attacker'
    # loot = {"wood": 100, "clay": 100, "iron": 100}
    #
    # battle_result = {"light_cavalry": 100}
    # save_battle_report(attacker_village_id,
    #                    defender_village_id,
    #                    units_to_attack,
    #                    defender_units,
    #                    winner,
    #                    battle_result,
    #                    loot)

    # Pass the reports to the template
    return render(request, 'plemiona/reports.html', {'reports': reports})