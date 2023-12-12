buildings_data_dict = {
    'sawmill': {
        1: {"wood": 50, "clay": 60, "iron": 40, "people_needed": 5, "total_population": 5, "performance": 15},
        2: {"wood": 63, "clay": 77, "iron": 50, "people_needed": 1, "total_population": 6, "performance": 17},
        3: {"wood": 78, "clay": 98, "iron": 63, "people_needed": 1, "total_population": 7, "performance": 20},
        4: {"wood": 98, "clay": 124, "iron": 77, "people_needed": 1, "total_population": 8, "performance": 23},
        5: {"wood": 122, "clay": 159, "iron": 96, "people_needed": 1, "total_population": 9, "performance": 27},

    },
    'clay_pit': {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 65, "clay": 50, "iron": 40, "people_needed": 10, "total_population": 10, "performance": 15},
        2: {"wood": 83, "clay": 63, "iron": 50, "people_needed": 1, "total_population": 11, "performance": 17},
        3: {"wood": 105, "clay": 80, "iron": 62, "people_needed": 2, "total_population": 13, "performance": 20},
        4: {"wood": 133, "clay": 101, "iron": 76, "people_needed": 2, "total_population": 15, "performance": 23},
        5: {"wood": 169, "clay": 128, "iron": 95, "people_needed": 2, "total_population": 17, "performance": 27},

    },
    'iron_mine': {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 75, "clay": 65, "iron": 70, "people_needed": 10, "total_population": 10, "performance": 15},
        2: {"wood": 94, "clay": 83, "iron": 87, "people_needed": 2, "total_population": 12, "performance": 17},
        3: {"wood": 118, "clay": 106, "iron": 108, "people_needed": 2, "total_population": 14, "performance": 20},
        4: {"wood": 147, "clay": 135, "iron": 133, "people_needed": 2, "total_population": 16, "performance": 23},
        5: {"wood": 184, "clay": 172, "iron": 165, "people_needed": 3, "total_population": 19, "performance": 27},

    },
    'granary': {
        1: {"wood": 60, "clay": 50, "iron": 40, "people_needed": 0, "total_population": 0, "capacity": 1000},
        2: {"wood": 76, "clay": 64, "iron": 50, "people_needed": 0, "total_population": 0, "capacity": 1229},
        3: {"wood": 96, "clay": 81, "iron": 62, "people_needed": 0, "total_population": 0, "capacity": 1512},
        4: {"wood": 121, "clay": 102, "iron": 77, "people_needed": 0, "total_population": 0, "capacity": 1859},
        5: {"wood": 154, "clay": 130, "iron": 96, "people_needed": 0, "total_population": 0, "capacity": 2285},

    },
    'town_hall': {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 90, "clay": 80, "iron": 70, "people_needed": 5, "total_population": 5, "build_time": 95},
        2: {"wood": 113, "clay": 102, "iron": 88, "people_needed": 1, "total_population": 6, "build_time": 91},
        3: {"wood": 143, "clay": 130, "iron": 111, "people_needed": 1, "total_population": 7, "build_time": 86},
        4: {"wood": 180, "clay": 166, "iron": 140, "people_needed": 1, "total_population": 8, "build_time": 82},
        5: {"wood": 227, "clay": 211, "iron": 176, "people_needed": 1, "total_population": 9, "build_time": 78},

    },
    'barracks': {
        1: {"wood": 200, "clay": 170, "iron": 90, "peolpe_needed": 7, "total_population": 7, "performace": "63%"},
        2: {"wood": 252, "clay": 218, "iron": 113, "peolpe_needed": 1, "total_population": 8, "performace": "59%"},
        3: {"wood": 318, "clay": 279, "iron": 143, "peolpe_needed": 2, "total_population": 10, "performace": "56%"},
        4: {"wood": 400, "clay": 357, "iron": 180, "peolpe_needed": 1, "total_population": 11, "performace": "53%"},

    },
    "stable": {
        1: {"wood": 270, "clay": 240, "iron": 260, "peolpe_needed": 8, "total_population": 8, "performance": 63},
        2: {"wood": 340, "clay": 307, "iron": 328, "peolpe_needed": 1, "total_population": 9, "performance": 59},
        3: {"wood": 429, "clay": 393, "iron": 413, "peolpe_needed": 2, "total_population": 11, "performance": 56},
        4: {"wood": 540, "clay": 503, "iron": 520, "peolpe_needed": 2, "total_population": 13, "performance": 53},
    },
    "workshop": {
        1: {"wood": 300, "clay": 240, "iron": 260, "people_needed": 8, "total_population": 8, "performance": 63},
        2: {"wood": 378, "clay": 307, "iron": 328, "people_needed": 1, "total_population": 9, "performance": 59},
        3: {"wood": 476, "clay": 393, "iron": 413, "people_needed": 2, "total_population": 11, "performance": 56},
        4: {"wood": 600, "clay": 503, "iron": 520, "people_needed": 2, "total_population": 13, "performance": 53},
        5: {"wood": 756, "clay": 644, "iron": 655, "people_needed": 2, "total_population": 15, "performance": 50},

    },
    "forge": {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 220, "clay": 180, "iron": 240, "people_needed": 20, "total_population": 20, "time_factor": 91},
        2: {"wood": 277, "clay": 229, "iron": 302, "people_needed": 3, "total_population": 23, "time_factor": 83},
        3: {"wood": 349, "clay": 293, "iron": 381, "people_needed": 4, "total_population": 27, "time_factor": 75},
        4: {"wood": 440, "clay": 373, "iron": 480, "people_needed": 5, "total_population": 32, "time_factor": 68},
        5: {"wood": 555, "clay": 476, "iron": 605, "people_needed": 5, "total_population": 37, "time_factor": 62},

    },
    "market": {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 100, "clay": 100, "iron": 100, "people_needed": 20, "total_population": 20, "merchants": 1},
        2: {"wood": 126, "clay": 127, "iron": 126, "people_needed": 3, "total_population": 23, "merchants": 2},
        3: {"wood": 159, "clay": 163, "iron": 159, "people_needed": 4, "total_population": 27, "merchants": 3},
        4: {"wood": 200, "clay": 207, "iron": 200, "people_needed": 5, "total_population": 32, "merchants": 4},

    },
    "farm": {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 45, "clay": 40, "iron": 30, "people_needed": 0, "total_population": 0, "max_population": 240},
        2: {"wood": 59, "clay": 53, "iron": 39, "people_needed": 0, "total_population": 0, "max_population": 281},
        3: {"wood": 76, "clay": 70, "iron": 50, "people_needed": 0, "total_population": 0, "max_population": 329},
        4: {"wood": 99, "clay": 92, "iron": 64, "people_needed": 0, "total_population": 0, "max_population": 386},

    },
    "wall": {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 50, "clay": 100, "iron": 20, "people_needed": 5, "total_population": 5, "defense_factor": 4},
        2: {"wood": 63, "clay": 127, "iron": 25, "people_needed": 1, "total_population": 6, "defense_factor": 8},
        3: {"wood": 79, "clay": 163, "iron": 32, "people_needed": 1, "total_population": 7, "defense_factor": 12},
        4: {"wood": 100, "clay": 207, "iron": 40, "people_needed": 1, "total_population": 8, "defense_factor": 16},
        5: {"wood": 126, "clay": 264, "iron": 50, "people_needed": 1, "total_population": 9, "defense_factor": 20},

    },
    "cache": {  # Zastąp "building_name" właściwą nazwą budynku
        1: {"wood": 50, "clay": 60, "iron": 50, "people_needed": 2, "total_population": 2, "hidden_resources": 150},
        2: {"wood": 63, "clay": 75, "iron": 63, "people_needed": 0, "total_population": 2, "hidden_resources": 200},
        3: {"wood": 78, "clay": 94, "iron": 78, "people_needed": 1, "total_population": 3, "hidden_resources": 267},
        4: {"wood": 98, "clay": 117, "iron": 98, "people_needed": 0, "total_population": 3, "hidden_resources": 356},

    },
    "palace": {
        1: {"wood": 15000, "clay": 25000, "iron": 10000, "people_needed": 80, "total_population": 80, "performance": 63}

    }

}
