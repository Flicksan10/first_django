buildings_data_dict = {
    'sawmill': {
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 5},
        1: {"wood": 50, "clay": 60, "iron": 40, "people_needed": 5, "total_population": 5, "performance": 15},
        2: {"wood": 63, "clay": 77, "iron": 50, "people_needed": 1, "total_population": 6, "performance": 17},
        3: {"wood": 78, "clay": 98, "iron": 63, "people_needed": 1, "total_population": 7, "performance": 20},
        4: {"wood": 98, "clay": 124, "iron": 77, "people_needed": 1, "total_population": 8, "performance": 23},
        5: {"wood": 122, "clay": 159, "iron": 96, "people_needed": 1, "total_population": 9, "performance": 27},
        6: {"wood": 153, "clay": 202, "iron": 120, "people_needed": 1, "total_population": 10, "performance": 32},
        7: {"wood": 191, "clay": 258, "iron": 149, "people_needed": 2, "total_population": 12, "performance": 37},
        8: {"wood": 238, "clay": 329, "iron": 185, "people_needed": 2, "total_population": 14, "performance": 43},
        9: {"wood": 298, "clay": 419, "iron": 231, "people_needed": 2, "total_population": 16, "performance": 50},
        10: {"wood": 373, "clay": 534, "iron": 287, "people_needed": 2, "total_population": 18, "performance": 58},
        11: {"wood": 466, "clay": 681, "iron": 358, "people_needed": 3, "total_population": 21, "performance": 68},
        12: {"wood": 582, "clay": 868, "iron": 446, "people_needed": 3, "total_population": 24, "performance": 79},
        13: {"wood": 728, "clay": 1107, "iron": 555, "people_needed": 4, "total_population": 28, "performance": 92},
        14: {"wood": 909, "clay": 1412, "iron": 691, "people_needed": 5, "total_population": 33, "performance": 107},
        15: {"wood": 1137, "clay": 1800, "iron": 860, "people_needed": 5, "total_population": 38, "performance": 249},
        16: {"wood": 1421, "clay": 2295, "iron": 1071, "people_needed": 5, "total_population": 43, "performance": 144},
        17: {"wood": 1776, "clay": 2926, "iron": 1333, "people_needed": 7, "total_population": 50, "performance": 168},
        18: {"wood": 2220, "clay": 3731, "iron": 1659, "people_needed": 8, "total_population": 58, "performance": 145},
        19: {"wood": 2776, "clay": 4757, "iron": 2066, "people_needed": 9, "total_population": 67, "performance": 227},
        20: {"wood": 3469, "clay": 6065, "iron": 2572, "people_needed": 10, "total_population": 77, "performance": 265},
        21: {"wood": 4337, "clay": 7733, "iron": 3202, "people_needed": 12, "total_population": 89, "performance": 308},
        22: {"wood": 5421, "clay": 9860, "iron": 3987, "people_needed": 14, "total_population": 103, "performance": 358},
        23: {"wood": 6776, "clay": 12571, "iron": 4963, "people_needed": 16, "total_population": 119, "performance": 416},
        24: {"wood": 8470, "clay": 16028, "iron": 6180, "people_needed": 19, "total_population": 138, "performance": 484},
        25: {"wood": 10588, "clay": 20436, "iron": 7694, "people_needed": 21, "total_population": 159, "performance": 563},
        26: {"wood": 13235, "clay": 26056, "iron": 9578, "people_needed": 24, "total_population": 183, "performance": 655},
        27: {"wood": 16544, "clay": 33221, "iron": 11925, "people_needed": 29, "total_population": 212, "performance": 762},
        28: {"wood": 20680, "clay": 42357, "iron": 14847, "people_needed": 33, "total_population": 245, "performance": 887},
        29: {"wood": 25849, "clay": 54005, "iron": 18484, "people_needed": 38, "total_population": 283, "performance": 1031},
        30: {"wood": 32312, "clay": 68857, "iron": 23013, "people_needed": 43, "total_population": 326, "performance": 1200}
    },
    'clay_pit': {  # Zastąp "building_name" właściwą nazwą budynku
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 5},
        1: {"wood": 65, "clay": 50, "iron": 40, "people_needed": 10, "total_population": 10, "performance": 15},
        2: {"wood": 83, "clay": 63, "iron": 50, "people_needed": 1, "total_population": 11, "performance": 17},
        3: {"wood": 105, "clay": 80, "iron": 62, "people_needed": 2, "total_population": 13, "performance": 20},
        4: {"wood": 133, "clay": 101, "iron": 76, "people_needed": 2, "total_population": 15, "performance": 23},
        5: {"wood": 169, "clay": 128, "iron": 95, "people_needed": 2, "total_population": 17, "performance": 27},
        6: {"wood": 215, "clay": 162, "iron": 117, "people_needed": 2, "total_population": 19, "performance": 32},
        7: {"wood": 273, "clay": 205, "iron": 145, "people_needed": 3, "total_population": 22, "performance": 37},
        8: {"wood": 346, "clay": 259, "iron": 180, "people_needed": 3, "total_population": 25, "performance": 43},
        9: {"wood": 440, "clay": 328, "iron": 224, "people_needed": 4, "total_population": 29, "performance": 50},
        10: {"wood": 559, "clay": 415, "iron": 277, "people_needed": 4, "total_population": 33, "performance": 58},
        11: {"wood": 709, "clay": 525, "iron": 344, "people_needed": 4, "total_population": 37, "performance": 68},
        12: {"wood": 901, "clay": 664, "iron": 426, "people_needed": 5, "total_population": 42, "performance": 79},
        13: {"wood": 1144, "clay": 840, "iron": 529, "people_needed": 6, "total_population": 48, "performance": 92},
        14: {"wood": 1453, "clay": 1062, "iron": 655, "people_needed": 7, "total_population": 55, "performance": 107},
        15: {"wood": 1846, "clay": 1343, "iron": 813, "people_needed": 8, "total_population": 63, "performance": 124},
        16: {"wood": 2344, "clay": 1700, "iron": 1008, "people_needed": 8, "total_population": 71, "performance": 144},
        17: {"wood": 2977, "clay": 2150, "iron": 1250, "people_needed": 10, "total_population": 81, "performance": 168},
        18: {"wood": 3781, "clay": 2720, "iron": 1550, "people_needed": 12, "total_population": 93, "performance": 195},
        19: {"wood": 4802, "clay": 3440, "iron": 1922, "people_needed": 13, "total_population": 103, "performance": 227},
        20: {"wood": 6098, "clay": 4352, "iron": 2383, "people_needed": 15, "total_population": 121, "performance": 265},
        21: {"wood": 7744, "clay": 5505, "iron": 2955, "people_needed": 16, "total_population": 137, "performance": 308},
        22: {"wood": 9835, "clay": 6964, "iron": 3664, "people_needed": 20, "total_population": 157, "performance": 358},
        23: {"wood": 12491, "clay": 8810, "iron": 4543, "people_needed": 22, "total_population": 179, "performance": 416},
        24: {"wood": 15863, "clay": 11144, "iron": 5633, "people_needed": 25, "total_population": 204, "performance": 484},
        25: {"wood": 20147, "clay": 14098, "iron": 6985, "people_needed": 28, "total_population": 232, "performance": 563},
        26: {"wood": 25586, "clay": 17833, "iron": 8662, "people_needed": 33, "total_population": 265, "performance": 655},
        27: {"wood": 32495, "clay": 22559, "iron": 10740, "people_needed": 37, "total_population": 302, "performance": 762},
        28: {"wood": 41268, "clay": 28537, "iron": 13318, "people_needed": 42, "total_population": 344, "performance": 887},
        29: {"wood": 52410, "clay": 36100, "iron": 16515, "people_needed": 48, "total_population": 392, "performance": 1031},
        30: {"wood": 66561, "clay": 45666, "iron": 20478, "people_needed": 55, "total_population": 447, "performance": 1200}
    },
        'iron_mine': {  # Zastąp "building_name" właściwą nazwą budynku
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 5},
        1: {"wood": 75, "clay": 65, "iron": 70, "people_needed": 10, "total_population": 10, "performance": 15},
        2: {"wood": 94, "clay": 83, "iron": 87, "people_needed": 2, "total_population": 12, "performance": 17},
        3: {"wood": 118, "clay": 106, "iron": 108, "people_needed": 2, "total_population": 14, "performance": 20},
        4: {"wood": 147, "clay": 135, "iron": 133, "people_needed": 2, "total_population": 16, "performance": 23},
        5: {"wood": 184, "clay": 172, "iron": 165, "people_needed": 3, "total_population": 19, "performance": 27},
        6: {"wood": 231, "clay": 219, "iron": 205, "people_needed": 3, "total_population": 22, "performance": 32},
        7: {"wood": 289, "clay": 279, "iron": 254, "people_needed": 4, "total_population": 26, "performance": 37},
        8: {"wood": 362, "clay": 352, "iron": 316, "people_needed": 4, "total_population": 30, "performance": 43},
        9: {"wood": 453, "clay": 454, "iron": 391, "people_needed": 5, "total_population": 35, "performance": 50},
        10: {"wood": 567, "clay": 579, "iron": 485, "people_needed": 6, "total_population": 41, "performance": 58},
        11: {"wood": 710, "clay": 738, "iron": 602, "people_needed": 7, "total_population": 48, "performance": 68},
        12: {"wood": 889, "clay": 941, "iron": 746, "people_needed": 8, "total_population": 56, "performance": 79},
        13: {"wood": 1113, "clay": 1200, "iron": 925, "people_needed": 10, "total_population": 66, "performance": 92},
        14: {"wood": 1393, "clay": 1529, "iron": 1147, "people_needed": 11, "total_population": 77, "performance": 107},
        15: {"wood": 1744, "clay": 1950, "iron": 1422, "people_needed": 13, "total_population": 90, "performance": 124},
        16: {"wood": 2183, "clay": 2486, "iron": 1764, "people_needed": 15, "total_population": 105, "performance": 144},
        17: {"wood": 2734, "clay": 3170, "iron": 2187, "people_needed": 18, "total_population": 123, "performance": 168},
        18: {"wood": 3422, "clay": 4042, "iron": 2712, "people_needed": 21, "total_population": 144, "performance": 195},
        19: {"wood": 4285, "clay": 5153, "iron": 3363, "people_needed": 25, "total_population": 169, "performance": 227},
        20: {"wood": 5365, "clay": 6571, "iron": 4170, "people_needed": 28, "total_population": 197, "performance": 265},
        21: {"wood": 6717, "clay": 8378, "iron": 5170, "people_needed": 34, "total_population": 231, "performance": 308},
        22: {"wood": 8409, "clay": 10681, "iron": 6411, "people_needed": 39, "total_population": 270, "performance": 358},
        23: {"wood": 10528, "clay": 13619, "iron": 7950, "people_needed": 46, "total_population": 316, "performance": 416},
        24: {"wood": 13181, "clay": 17364, "iron": 9858, "people_needed": 54, "total_population": 370, "performance": 484},
        25: {"wood": 15503, "clay": 22139, "iron": 12224, "people_needed": 63, "total_population": 433, "performance": 563},
        26: {"wood": 20662, "clay": 28227, "iron": 15158, "people_needed": 74, "total_population": 507, "performance": 655},
        27: {"wood": 25869, "clay": 35990, "iron": 18796, "people_needed": 86, "total_population": 593, "performance": 762},
        28: {"wood": 32388, "clay": 45887, "iron": 23307, "people_needed": 100, "total_population": 693, "performance": 887},
        29: {"wood": 40549, "clay": 58506, "iron": 28900, "people_needed": 118, "total_population": 811, "performance": 1031},
        30: {"wood": 50768, "clay": 74595, "iron": 35837, "people_needed": 138, "total_population": 949, "performance": 1200}
    },
    'granary':{
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 500},
        1: {"wood": 60, "clay": 50, "iron": 40, "people_needed": 0, "total_population": 0, "performance": 1000},
        2: {"wood": 76, "clay": 64, "iron": 50, "people_needed": 0, "total_population": 0, "performance": 1229},
        3: {"wood": 96, "clay": 81, "iron": 62, "people_needed": 0, "total_population": 0, "performance": 1512},
        4: {"wood": 121, "clay": 102, "iron": 77, "people_needed": 0, "total_population": 0, "performance": 1859},
        5: {"wood": 154, "clay": 130, "iron": 96, "people_needed": 0, "total_population": 0, "performance": 2285},
        6: {"wood": 194, "clay": 165, "iron": 120, "people_needed": 0, "total_population": 0, "performance": 2810},
        7: {"wood": 246, "clay": 229, "iron": 149, "people_needed": 0, "total_population": 0, "performance": 3454},
        8: {"wood": 311, "clay": 286, "iron": 185, "people_needed": 0, "total_population": 0, "performance": 4247},
        9: {"wood": 393, "clay": 358, "iron": 231, "people_needed": 0, "total_population": 0, "performance": 5222},
        10: {"wood": 498, "clay": 447, "iron": 287, "people_needed": 0, "total_population": 0, "performance": 6420},
        11: {"wood": 630, "clay": 546, "iron": 358, "people_needed": 0, "total_population": 0, "performance": 7893},
        12: {"wood": 796, "clay": 693, "iron": 446, "people_needed": 0, "total_population": 0, "performance": 9705},
        13: {"wood": 1007, "clay": 880, "iron": 555, "people_needed": 0, "total_population": 0, "performance": 11932},
        14: {"wood": 1274, "clay": 1180, "iron": 691, "people_needed": 0, "total_population": 0, "performance": 14670},
        15: {"wood": 1612, "clay": 1420, "iron": 860, "people_needed": 0, "total_population": 0, "performance": 18037},
        16: {"wood": 2039, "clay": 1803, "iron": 1071, "people_needed": 0, "total_population": 0, "performance": 22177},
        17: {"wood": 2580, "clay": 2290, "iron": 1333, "people_needed": 0, "total_population": 0, "performance": 27266},
        18: {"wood": 3264, "clay": 2908, "iron": 1659, "people_needed": 0, "total_population": 0, "performance": 33523},
        19: {"wood": 4128, "clay": 3693, "iron": 2066, "people_needed": 0, "total_population": 0, "performance": 41217},
        20: {"wood": 5222, "clay": 4691, "iron": 2572, "people_needed": 0, "total_population": 0, "performance": 50675},
        21: {"wood": 6606, "clay": 5957, "iron": 3202, "people_needed": 0, "total_population": 0, "performance": 62305},
        22: {"wood": 8357, "clay": 7599, "iron": 3987, "people_needed": 0, "total_population": 0, "performance": 76604},
        23: {"wood": 10572, "clay": 9608, "iron": 4963, "people_needed": 0, "total_population": 0, "performance": 94184},
        24: {"wood": 13373, "clay": 12203, "iron": 6180, "people_needed": 0, "total_population": 0, "performance": 115798},
        25: {"wood": 16917, "clay": 15497, "iron": 7694, "people_needed": 0, "total_population": 0, "performance": 142373},
        26: {"wood": 21400, "clay": 19682, "iron": 9578, "people_needed": 0, "total_population": 0, "performance": 175047},
        27: {"wood": 27071, "clay": 24996, "iron": 11925, "people_needed": 0, "total_population": 0, "performance": 215219},
        28: {"wood": 34245, "clay": 31745, "iron": 14847, "people_needed": 0, "total_population": 0, "performance": 264611},
        29: {"wood": 43320, "clay": 40316, "iron": 18484, "people_needed": 0, "total_population": 0, "performance": 325337},
        30: {"wood": 54799, "clay": 51201, "iron": 23013, "people_needed": 0, "total_population": 0, "performance": 400000}
    },
        'town_hall': {  # Zastąp "building_name" właściwą nazwą budynku
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 100},
        1: {"wood": 90, "clay": 80, "iron": 70, "people_needed": 5, "total_population": 5, "performance": 95},
        2: {"wood": 113, "clay": 102, "iron": 88, "people_needed": 1, "total_population": 6, "performance": 91},
        3: {"wood": 143, "clay": 130, "iron": 111, "people_needed": 1, "total_population": 7, "performance": 86},
        4: {"wood": 180, "clay": 166, "iron": 140, "people_needed": 1, "total_population": 8, "performance": 82},
        5: {"wood": 227, "clay": 211, "iron": 176, "people_needed": 1, "total_population": 9, "performance": 78},
        6: {"wood": 286, "clay": 270, "iron": 222, "people_needed": 2, "total_population": 11, "performance": 75},
        7: {"wood": 360, "clay": 344, "iron": 280, "people_needed": 2, "total_population": 13, "performance": 71},
        8: {"wood": 454, "clay": 438, "iron": 353, "people_needed": 2, "total_population": 15, "performance": 68},
        9: {"wood": 572, "clay": 559, "iron": 445, "people_needed": 3, "total_population": 18, "performance": 64},
        10: {"wood": 720, "clay": 712, "iron": 560, "people_needed": 3, "total_population": 21, "performance": 61},
        11: {"wood": 908, "clay": 908, "iron": 706, "people_needed": 3, "total_population": 24, "performance": 58},
        12: {"wood": 1144, "clay": 1158, "iron": 890, "people_needed": 4, "total_population": 28, "performance": 56},
        13: {"wood": 1441, "clay": 1476, "iron": 1121, "people_needed": 5, "total_population": 33, "performance": 53},
        14: {"wood": 1816, "clay": 1882, "iron": 1412, "people_needed": 5, "total_population": 38, "performance": 51},
        15: {"wood": 2288, "clay": 2400, "iron": 1779, "people_needed": 7, "total_population": 45, "performance": 48},
        16: {"wood": 2883, "clay": 3060, "iron": 2242, "people_needed": 8, "total_population": 53, "performance": 46},
        17: {"wood": 3632, "clay": 3902, "iron": 2825, "people_needed": 9, "total_population": 62, "performance": 44},
        18: {"wood": 4577, "clay": 4975, "iron": 3560, "people_needed": 10, "total_population": 72, "performance": 42},
        19: {"wood": 5767, "clay": 6343, "iron": 4485, "people_needed": 12, "total_population": 84, "performance": 40},
        20: {"wood": 7266, "clay": 8087, "iron": 5651, "people_needed": 15, "total_population": 99, "performance": 38},
        21: {"wood": 9155, "clay": 10311, "iron": 7120, "people_needed": 17, "total_population": 116, "performance": 36},
        22: {"wood": 11535, "clay": 13146, "iron": 8972, "people_needed": 19, "total_population": 135, "performance": 34},
        23: {"wood": 14534, "clay": 16762, "iron": 11304, "people_needed": 23, "total_population": 158, "performance": 33},
        24: {"wood": 18313, "clay": 21371, "iron": 14244, "people_needed": 27, "total_population": 185, "performance": 31},
        25: {"wood": 23075, "clay": 27248, "iron": 17947, "people_needed": 31, "total_population": 216, "performance": 30},
        26: {"wood": 29074, "clay": 34741, "iron": 22613, "people_needed": 37, "total_population": 253, "performance": 28},
        27: {"wood": 36633, "clay": 44295, "iron": 38493, "people_needed": 43, "total_population": 296, "performance": 27},
        28: {"wood": 46158, "clay": 56476, "iron": 35901, "people_needed": 51, "total_population": 347, "performance": 26},
        29: {"wood": 58159, "clay": 72007, "iron": 45235, "people_needed": 59, "total_population": 406, "performance": 24},
        30: {"wood": 73280, "clay": 91809, "iron": 56996, "people_needed": 69, "total_population": 475, "performance": 23}
},
    'barracks': {
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 100},
        1: {"wood": 200, "clay": 170, "iron": 90, "peolpe_needed": 7, "total_population": 7, "performance": 63},
        2: {"wood": 252, "clay": 218, "iron": 113, "peolpe_needed": 1, "total_population": 8, "performance": 59},
        3: {"wood": 318, "clay": 279, "iron": 143, "peolpe_needed": 2, "total_population": 10, "performance": 56},
        4: {"wood": 400, "clay": 357, "iron": 180, "peolpe_needed": 1, "total_population": 11, "performance": 53},
        5: {"wood": 504, "clay": 456, "iron": 227, "peolpe_needed": 2, "total_population": 13, "performance": 50},
        6: {"wood": 635, "clay": 584, "iron": 286, "peolpe_needed": 2, "total_population": 15, "performance": 47},
        7: {"wood": 800, "clay": 748, "iron": 360, "peolpe_needed": 3, "total_population": 18, "performance": 44},
        8: {"wood": 1.008, "clay": 957, "iron": 454, "peolpe_needed": 3, "total_population": 21, "performance": 42},
        9: {"wood": 1.271, "clay": 1.225, "iron": 572, "peolpe_needed": 4, "total_population": 25,
            "performance": 39},
        10: {"wood": 1.601, "clay": 1.568, "iron": 720, "peolpe_needed": 4, "total_population": 29,
             "performance": 37},
        11: {"wood": 2.017, "clay": 2.007, "iron": 908, "peolpe_needed": 5, "total_population": 34,
             "performance": 35},
        12: {"wood": 2.542, "clay": 2.569, "iron": 1.144, "peolpe_needed": 5, "total_population": 39,
             "performance": 33},
        13: {"wood": 3.202, "clay": 3.288, "iron": 1.441, "peolpe_needed": 7, "total_population": 46,
             "performance": 31},
        14: {"wood": 4.035, "clay": 4.209, "iron": 1.816, "peolpe_needed": 8, "total_population": 54,
             "performance": 29},
        15: {"wood": 5.084, "clay": 5.388, "iron": 2.288, "peolpe_needed": 9, "total_population": 63,
             "performance": 28},
        16: {"wood": 6.406, "clay": 6.896, "iron": 2.883, "peolpe_needed": 11, "total_population": 74,
             "performance": 26},
        17: {"wood": 8.072, "clay": 8.827, "iron": 3.632, "peolpe_needed": 12, "total_population": 86,
             "performance": 25},
        18: {"wood": 10.170, "clay": 11.298, "iron": 4.577, "peolpe_needed": 15, "total_population": 101,
             "performance": 23},
        19: {"wood": 12.814, "clay": 14.462, "iron": 5.767, "peolpe_needed": 17, "total_population": 118,
             "performance": 22},
        20: {"wood": 16.146, "clay": 18.511, "iron": 7.266, "peolpe_needed": 20, "total_population": 138,
             "performance": 21},
        21: {"wood": 20.344, "clay": 23.695, "iron": 9.155, "peolpe_needed": 24, "total_population": 162,
             "performance": 20},
        22: {"wood": 25.634, "clay": 30.329, "iron": 11.535, "peolpe_needed": 27, "total_population": 189,
             "performance": 19},
        23: {"wood": 32.298, "clay": 38.821, "iron": 14.534, "peolpe_needed": 32, "total_population": 221,
             "performance": 17},
        24: {"wood": 40.696, "clay": 49.691, "iron": 18.313, "peolpe_needed": 38, "total_population": 259,
             "performance": 16},
        25: {"wood": 51.277, "clay": 63.605, "iron": 23.075, "peolpe_needed": 44, "total_population": 303,
             "performance": 14},
    },
    "stable": {
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 100},
        1: {"wood": 270, "clay": 240, "iron": 260, "peolpe_needed": 8, "total_population": 8, "performance": 63},
        2: {"wood": 340, "clay": 307, "iron": 328, "peolpe_needed": 1, "total_population": 9, "performance": 59},
        3: {"wood": 429, "clay": 393, "iron": 413, "peolpe_needed": 2, "total_population": 11, "performance": 56},
        4: {"wood": 540, "clay": 503, "iron": 520, "peolpe_needed": 2, "total_population": 13, "performance": 53},
        5: {"wood": 681, "clay": 644, "iron": 655, "peolpe_needed": 2, "total_population": 15, "performance": 50},
        6: {"wood": 857, "clay": 825, "iron": 826, "peolpe_needed": 3, "total_population": 18, "performance": 47},
        7: {"wood": 1.080, "clay": 1.056, "iron": 1.040, "peolpe_needed": 3, "total_population": 21, "performance": 44},
        8: {"wood": 1.361, "clay": 1.351, "iron": 1.311, "peolpe_needed": 3, "total_population": 24, "performance": 42},
        9: {"wood": 1.715, "clay": 1.729, "iron": 1.652, "peolpe_needed": 4, "total_population": 28, "performance": 39},
        10: {"wood": 2.161, "clay": 2.214, "iron": 2.081, "peolpe_needed": 5, "total_population": 33,
             "performance": 37},
        11: {"wood": 2.723, "clay": 2.833, "iron": 2.622, "peolpe_needed": 5, "total_population": 38,
             "performance": 35},
        12: {"wood": 3.431, "clay": 3.627, "iron": 3.304, "peolpe_needed": 7, "total_population": 45,
             "performance": 33},
        13: {"wood": 4.323, "clay": 4.642, "iron": 4.163, "peolpe_needed": 8, "total_population": 53,
             "performance": 31},
        14: {"wood": 5.447, "clay": 5.942, "iron": 5.246, "peolpe_needed": 9, "total_population": 62,
             "performance": 29},
        15: {"wood": 6.864, "clay": 7.606, "iron": 6.609, "peolpe_needed": 10, "total_population": 72,
             "performance": 28},
        16: {"wood": 8.648, "clay": 9.736, "iron": 8.328, "peolpe_needed": 12, "total_population": 84,
             "performance": 26},
        17: {"wood": 10.897, "clay": 12.462, "iron": 10.493, "peolpe_needed": 15, "total_population": 99,
             "performance": 25},
        18: {"wood": 13.730, "clay": 15.951, "iron": 13.221, "peolpe_needed": 16, "total_population": 115,
             "performance": 23},
        19: {"wood": 17.300, "clay": 20.417, "iron": 16.659, "peolpe_needed": 20, "total_population": 135,
             "performance": 22},
        20: {"wood": 21.797, "clay": 26.134, "iron": 20.990, "peolpe_needed": 23, "total_population": 158,
             "performance": 21}},
    "workshop": {
    0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 100},
    1: {"wood": 300, "clay": 240, "iron": 260, "people_needed": 8, "total_population": 8, "performance": 63},
    2: {"wood": 378, "clay": 307, "iron": 328, "people_needed": 1, "total_population": 9, "performance": 59},
    3: {"wood": 476, "clay": 393, "iron": 413, "people_needed": 2, "total_population": 11, "performance": 56},
    4: {"wood": 600, "clay": 503, "iron": 520, "people_needed": 2, "total_population": 13, "performance": 53},
    5: {"wood": 756, "clay": 644, "iron": 655, "people_needed": 2, "total_population": 15, "performance": 50},
    6: {"wood": 953, "clay": 825, "iron": 826, "people_needed": 3, "total_population": 18, "performance": 47},
    7: {"wood": 1200, "clay": 1056, "iron": 1040, "people_needed": 3, "total_population": 21, "performance": 44},
    8: {"wood": 1513, "clay": 1351, "iron": 1311, "people_needed": 3, "total_population": 24, "performance": 42},
    9: {"wood": 1906, "clay": 1729, "iron": 1652, "people_needed": 4, "total_population": 28, "performance": 39},
    10: {"wood": 2401, "clay": 2214, "iron": 2081, "people_needed": 5, "total_population": 33, "performance": 37},
    11: {"wood": 3026, "clay": 2833, "iron": 2622, "people_needed": 5, "total_population": 38, "performance": 35},
    12: {"wood": 3812, "clay": 3627, "iron": 3304, "people_needed": 7, "total_population": 45, "performance": 33},
    13: {"wood": 4804, "clay": 4642, "iron": 4163, "people_needed": 8, "total_population": 53, "performance": 31},
    14: {"wood": 6053, "clay": 5942, "iron": 5246, "people_needed": 9, "total_population": 62, "performance": 29},
    15: {"wood": 7626, "clay": 7606, "iron": 6609, "people_needed": 10, "total_population": 72, "performance": 28}
    },
    "forge": {  # Zastąp "building_name" właściwą nazwą budynku
    0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 100},
    1: {"wood": 220, "clay": 180, "iron": 240, "people_needed": 20, "total_population": 20, "performance": 91},
    2: {"wood": 277, "clay": 229, "iron": 302, "people_needed": 3, "total_population": 23, "performance": 83},
    3: {"wood": 349, "clay": 293, "iron": 381, "people_needed": 4, "total_population": 27, "performance": 75},
    4: {"wood": 440, "clay": 373, "iron": 480, "people_needed": 5, "total_population": 32, "performance": 68},
    5: {"wood": 555, "clay": 476, "iron": 605, "people_needed": 5, "total_population": 37, "performance": 62},
    6: {"wood": 699, "clay": 606, "iron": 762, "people_needed": 7, "total_population": 44, "performance": 56},
    7: {"wood": 880, "clay": 773, "iron": 960, "people_needed": 7, "total_population": 51, "performance": 51},
    8: {"wood": 1109, "clay": 986, "iron": 1210, "people_needed": 9, "total_population": 60, "performance": 47},
    9: {"wood": 1398, "clay": 1257, "iron": 1525, "people_needed": 10, "total_population": 70, "performance": 42},
    10: {"wood": 1761, "clay": 1603, "iron": 1921, "people_needed": 12, "total_population": 82, "performance": 39},
    11: {"wood": 2219, "clay": 2043, "iron": 2421, "people_needed": 14, "total_population": 96, "performance": 35},
    12: {"wood": 2796, "clay": 2605, "iron": 3050, "people_needed": 16, "total_population": 112, "performance": 32},
    13: {"wood": 3523, "clay": 3322, "iron": 3843, "people_needed": 20, "total_population": 132, "performance": 29},
    14: {"wood": 4439, "clay": 4236, "iron": 4842, "people_needed": 22, "total_population": 154, "performance": 26},
    15: {"wood": 5593, "clay": 5400, "iron": 6101, "people_needed": 26, "total_population": 180, "performance": 24},
    16: {"wood": 7047, "clay": 6885, "iron": 7687, "people_needed": 31, "total_population": 211, "performance": 22},
    17: {"wood": 8879, "clay": 8779, "iron": 9686, "people_needed": 36, "total_population": 247, "performance": 20},
    18: {"wood": 11187, "clay": 11193, "iron": 12204, "people_needed": 42, "total_population": 289, "performance": 18},
    19: {"wood": 14096, "clay": 14271, "iron": 15377, "people_needed": 49, "total_population": 338, "performance": 16},
    20: {"wood": 17761, "clay": 18196, "iron": 19375, "people_needed": 57, "total_population": 395, "performance": 15}
    },
    "market": {  # Zastąp "building_name" właściwą nazwą budynku
    0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 0},
    1: {"wood": 100, "clay": 100, "iron": 100, "people_needed": 20, "total_population": 20, "performance": 1},
    2: {"wood": 126, "clay": 127, "iron": 126, "people_needed": 3, "total_population": 23, "performance": 2},
    3: {"wood": 159, "clay": 163, "iron": 159, "people_needed": 4, "total_population": 27, "performance": 3},
    4: {"wood": 200, "clay": 207, "iron": 200, "people_needed": 5, "total_population": 32, "performance": 4},
    5: {"wood": 252, "clay": 264, "iron": 252, "people_needed": 5, "total_population": 37, "performance": 5},
    6: {"wood": 318, "clay": 337, "iron": 318, "people_needed": 7, "total_population": 44, "performance": 6},
    7: {"wood": 400, "clay": 430, "iron": 400, "people_needed": 7, "total_population": 51, "performance": 7},
    8: {"wood": 504, "clay": 548, "iron": 504, "people_needed": 9, "total_population": 60, "performance": 8},
    9: {"wood": 635, "clay": 698, "iron": 635, "people_needed": 10, "total_population": 70, "performance": 9},
    10: {"wood": 800, "clay": 890, "iron": 800, "people_needed": 12, "total_population": 82, "performance": 10},
    11: {"wood": 1009, "clay": 1135, "iron": 1009, "people_needed": 14, "total_population": 96, "performance": 11},
    12: {"wood": 1271, "clay": 1447, "iron": 1271, "people_needed": 16, "total_population": 112, "performance": 14},
    13: {"wood": 1601, "clay": 1846, "iron": 1601, "people_needed": 20, "total_population": 132, "performance": 19},
    14: {"wood": 2018, "clay": 2353, "iron": 2018, "people_needed": 22, "total_population": 154, "performance": 26},
    15: {"wood": 2542, "clay": 3000, "iron": 2542, "people_needed": 26, "total_population": 180, "performance": 35},
    16: {"wood": 3203, "clay": 3825, "iron": 3203, "people_needed": 31, "total_population": 211, "performance": 46},
    17: {"wood": 4036, "clay": 4877, "iron": 4036, "people_needed": 36, "total_population": 247, "performance": 59},
    18: {"wood": 5085, "clay": 6218, "iron": 5085, "people_needed": 42, "total_population": 289, "performance": 74},
    19: {"wood": 6407, "clay": 7928, "iron": 6407, "people_needed": 49, "total_population": 338, "performance": 91},
    20: {"wood": 8073, "clay": 10109, "iron": 8073, "people_needed": 57, "total_population": 395, "performance": 110},
    21: {"wood": 10172, "clay": 12889, "iron": 10172, "people_needed": 67, "total_population": 462, "performance": 131},
    22: {"wood": 12817, "clay": 16433, "iron": 12817, "people_needed": 79, "total_population": 541, "performance": 154},
    23: {"wood": 16149, "clay": 20952, "iron": 16149, "people_needed": 92, "total_population": 633, "performance": 179},
    24: {"wood": 20348, "clay": 26714, "iron": 20348, "people_needed": 107, "total_population": 740, "performance": 206},
    25: {"wood": 25639, "clay": 34060, "iron": 25639, "people_needed": 126, "total_population": 866, "performance": 235}
},
    "farm": {  # Zastąp "building_name" właściwą nazwą budynku
    0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 100},
    1: {"wood": 45, "clay": 40, "iron": 30, "people_needed": 0, "total_population": 0, "performance": 240},
    2: {"wood": 59, "clay": 53, "iron": 39, "people_needed": 0, "total_population": 0, "performance": 281},
    3: {"wood": 76, "clay": 70, "iron": 50, "people_needed": 0, "total_population": 0, "performance": 329},
    4: {"wood": 99, "clay": 92, "iron": 64, "people_needed": 0, "total_population": 0, "performance": 386},
    5: {"wood": 129, "clay": 121, "iron": 83, "people_needed": 0, "total_population": 0, "performance": 452},
    6: {"wood": 167, "clay": 160, "iron": 107, "people_needed": 0, "total_population": 0, "performance": 530},
    7: {"wood": 217, "clay": 212, "iron": 138, "people_needed": 0, "total_population": 0, "performance": 622},
    8: {"wood": 282, "clay": 279, "iron": 178, "people_needed": 0, "total_population": 0, "performance": 729},
    9: {"wood": 367, "clay": 369, "iron": 230, "people_needed": 0, "total_population": 0, "performance": 854},
    10: {"wood": 477, "clay": 487, "iron": 297, "people_needed": 0, "total_population": 0, "performance": 1002},
    11: {"wood": 620, "clay": 642, "iron": 383, "people_needed": 0, "total_population": 0, "performance": 1174},
    12: {"wood": 806, "clay": 848, "iron": 494, "people_needed": 0, "total_population": 0, "performance": 1376},
    13: {"wood": 1048, "clay": 1119, "iron": 637, "people_needed": 0, "total_population": 0, "performance": 1613},
    14: {"wood": 1363, "clay": 1477, "iron": 822, "people_needed": 0, "total_population": 0, "performance": 1891},
    15: {"wood": 1772, "clay": 1950, "iron": 1060, "people_needed": 0, "total_population": 0, "performance": 2216},
    16: {"wood": 2303, "clay": 2574, "iron": 1368, "people_needed": 0, "total_population": 0, "performance": 2598},
    17: {"wood": 2994, "clay": 3398, "iron": 1764, "people_needed": 0, "total_population": 0, "performance": 3045},
    18: {"wood": 3893, "clay": 4486, "iron": 2276, "people_needed": 0, "total_population": 0, "performance": 3569},
    19: {"wood": 5060, "clay": 5921, "iron": 2936, "people_needed": 0, "total_population": 0, "performance": 4183},
    20: {"wood": 6579, "clay": 7816, "iron": 3787, "people_needed": 0, "total_population": 0, "performance": 4904},
    21: {"wood": 8525, "clay": 10317, "iron": 4886, "people_needed": 0, "total_population": 0, "performance": 5748},
    22: {"wood": 11118, "clay": 13618, "iron": 6302, "people_needed": 0, "total_population": 0, "performance": 6737},
    23: {"wood": 14453, "clay": 17976, "iron": 8130, "people_needed": 0, "total_population": 0, "performance": 7896},
    24: {"wood": 18789, "clay": 23728, "iron": 10488, "people_needed": 0, "total_population": 0, "performance": 9255},
    25: {"wood": 24426, "clay": 31321, "iron": 13529, "people_needed": 0, "total_population": 0, "performance": 10848},
    26: {"wood": 31754, "clay": 41344, "iron": 17453, "people_needed": 0, "total_population": 0, "performance": 12715},
    27: {"wood": 41280, "clay": 54574, "iron": 22514, "people_needed": 0, "total_population": 0, "performance": 14904},
    28: {"wood": 53664, "clay": 72037, "iron": 29043, "people_needed": 0, "total_population": 0, "performance": 17469},
    29: {"wood": 69763, "clay": 95089, "iron": 37466, "people_needed": 0, "total_population": 0, "performance": 20476},
    30: {"wood": 90692, "clay": 125517, "iron": 48331, "people_needed": 0, "total_population": 0, "performance": 24000}
},
    "wall": {  # Zastąp "building_name" właściwą nazwą budynku
    0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 1},
        1: {"wood": 50, "clay": 100, "iron": 20, "people_needed": 5, "total_population": 5, "performance": 4},
        2: {"wood": 63, "clay": 127, "iron": 25, "people_needed": 1, "total_population": 6, "performance": 8},
        3: {"wood": 79, "clay": 163, "iron": 32, "people_needed": 1, "total_population": 7, "performance": 12},
        4: {"wood": 100, "clay": 207, "iron": 40, "people_needed": 1, "total_population": 8, "performance": 16},
        5: {"wood": 126, "clay": 264, "iron": 50, "people_needed": 1, "total_population": 9, "performance": 20},
        6: {"wood": 159, "clay": 337, "iron": 64, "people_needed": 2, "total_population": 11, "performance": 24},
        7: {"wood": 200, "clay": 430, "iron": 80, "people_needed": 2, "total_population": 13, "performance": 29},
        8: {"wood": 252, "clay": 548, "iron": 101, "people_needed": 2, "total_population": 15, "performance": 34},
        9: {"wood": 318, "clay": 698, "iron": 127, "people_needed": 3, "total_population": 18, "performance": 39},
        10: {"wood": 400, "clay": 890, "iron": 160, "people_needed": 3, "total_population": 21, "performance": 44},
        11: {"wood": 504, "clay": 1135, "iron": 202, "people_needed": 3, "total_population": 24, "performance": 49},
        12: {"wood": 635, "clay": 1447, "iron": 254, "people_needed": 4, "total_population": 28, "performance": 55},
        13: {"wood": 801, "clay": 1846, "iron": 320, "people_needed": 5, "total_population": 33, "performance": 60},
        14: {"wood": 1009, "clay": 2353, "iron": 404, "people_needed": 5, "total_population": 38, "performance": 66},
        15: {"wood": 1271, "clay": 3000, "iron": 508, "people_needed": 7, "total_population": 45, "performance": 72},
        16: {"wood": 1602, "clay": 3825, "iron": 641, "people_needed": 8, "total_population": 53, "performance": 79},
        17: {"wood": 2018, "clay": 4877, "iron": 807, "people_needed": 9, "total_population": 62, "performance": 85},
        18: {"wood": 2543, "clay": 6218, "iron": 1017, "people_needed": 10, "total_population": 72, "performance": 92},
        19: {"wood": 3204, "clay": 7928, "iron": 1281, "people_needed": 12, "total_population": 84, "performance": 99},
        20: {"wood": 4037, "clay": 10109, "iron": 1615, "people_needed": 15, "total_population": 99, "performance": 107}
    },
    "cache": {  # Zastąp "building_name" właściwą nazwą budynku
    0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 50},
        1: {"wood": 50, "clay": 60, "iron": 50, "people_needed": 2, "total_population": 2, "performance": 150},
        2: {"wood": 63, "clay": 75, "iron": 63, "people_needed": 0, "total_population": 2, "performance": 200},
        3: {"wood": 78, "clay": 94, "iron": 78, "people_needed": 1, "total_population": 3, "performance": 267},
        4: {"wood": 98, "clay": 117, "iron": 98, "people_needed": 0, "total_population": 3, "performance": 356},
        5: {"wood": 122, "clay": 146, "iron": 122, "people_needed": 1, "total_population": 4, "performance": 474},
        6: {"wood": 153, "clay": 183, "iron": 153, "people_needed": 0, "total_population": 4, "performance": 632},
        7: {"wood": 191, "clay": 229, "iron": 191, "people_needed": 1, "total_population": 5, "performance": 843},
        8: {"wood": 238, "clay": 286, "iron": 238, "people_needed": 1, "total_population": 6, "performance": 1125},
        9: {"wood": 298, "clay": 358, "iron": 298, "people_needed": 1, "total_population": 7, "performance": 1500},
        10: {"wood": 373, "clay": 447, "iron": 373, "people_needed": 1, "total_population": 8, "performance": 2000}
},
    "palace" : {
        0: {"wood": 0, "clay": 0, "iron": 0, "people_needed": 0, "total_population": 0, "performance": 0},
        1: {"wood": 15000, "clay": 25000, "iron": 10000, "people_needed": 80, "total_population": 80, "performance": 63}

    }

}
