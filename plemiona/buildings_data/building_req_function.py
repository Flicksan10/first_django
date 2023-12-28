def check_building_requirements(village, building_type, buildings_lvl_requirements):
    """
    Check if the building meets the level requirements for upgrade.

    :param village: Village object containing current levels of buildings.
    :param building_type: Type of building to be upgraded.
    :param buildings_lvl_requirements: Dictionary of building requirements.
    :return: Boolean indicating if requirements are met and a message.
    """
    # Check if the building has any requirements
    requirements = buildings_lvl_requirements.get(building_type, {})

    # If there are no requirements, the building can be upgraded
    if not requirements:
        return True, "No requirements for this building."

    # Check each requirement
    for required_building, required_level in requirements.items():
        # Get the current level of the required building
        current_level = getattr(village, required_building, 0)
        if current_level < required_level:
            return False, f"{required_building.capitalize()} needs to be at level {required_level}."

    # If all requirements are met
    return True, "All requirements met."