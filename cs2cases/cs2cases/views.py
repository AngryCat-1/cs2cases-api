import json
import random

from django.http import JsonResponse
import datetime
from cs2cases.cases import *


def open_case(request):
    classes = [CaseKilovat, CaseCS16, CaseCSGO, CaseDangerZone]
    json_end_answer = {}
    count = 1
    is_specifed_case = True
    is_specifed_case_instance = False
    if "count" in request.GET:
        count = int(request.GET['count'])
        print(count)

    if "id" in request.GET:
        caseid = request.GET['id']
        classes_by_name = {cls.__name__: cls for cls in classes}
        target_case = classes_by_name.get(caseid)
        if target_case is None:
            return JsonResponse({"Результат" :"Кейса с этим именем не существует"})
    else:
        is_specifed_case = False


    for i in range(0, count):
        i += 1
        if not is_specifed_case:
            target_case = random.choice(classes)
        price = 25
        if not is_specifed_case_instance:
            target_case = target_case()
            is_specifed_case_instance = True

        int_random_rare = random.randint(0,100000)/1000
        is_statrack = False
        blue_class = next((cls for cls in target_case.drops if getattr(cls, 'rare', None) == 'blue'), None)
        fiolet_class = next((cls for cls in target_case.drops if getattr(cls, 'rare', None) == 'fiolet'), None)
        pink_class = next((cls for cls in target_case.drops if getattr(cls, 'rare', None) == 'pink'), None)
        red_class = next((cls for cls in target_case.drops if getattr(cls, 'rare', None) == 'red'), None)
        gold_class = next((cls for cls in target_case.drops if getattr(cls, 'rare', None) == 'gold'), None)

        if int_random_rare < target_case.chance_gold:
            SkinClass = gold_class()
        elif int_random_rare < target_case.chance_red:
            SkinClass = red_class()
        elif int_random_rare < target_case.chance_pink:
            SkinClass = pink_class()
        elif int_random_rare < target_case.chance_fiolet:
            SkinClass = fiolet_class()
        else:
            SkinClass = blue_class

        skin_float = random.random()
        pattern = random.randint(1,1000)

        if target_case.name == "CaseCS16":
            price *= 0.90
        elif target_case.name == "CaseKilovat":
            price *= 1.15
        elif target_case.name == "CaseDangerZone":
            price *= 1.40
        elif target_case.name == "CaseCS2":
            price *= 1.75

        if SkinClass.rare == "blue":
            price *= 3
        elif SkinClass.rare == "fiolet":
            price *= 25
        elif SkinClass.rare == "pink":
            price *= 150
        elif SkinClass.rare == "red":
            price *= 400
        elif SkinClass.rare == "gold":
            price *= 1500

        a = 0.29894885546288075
        b = 1.0035161350107586
        skin_float_price_multiplayer = a * (b ** skin_float)
        if skin_float_price_multiplayer > 0.8:
            price *= skin_float_price_multiplayer
        else:
            price *= 0.8

        rare_patterns = [1, 7, 51, 100, 101, 105, 125, 140, 290, 291, 299, 356, 357, 389, 460, 492, 581, 602, 795, 790, 800, 801, 802, 803, 856, 893, 899,
                         900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925,
                         978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]

        so_rare_patterns = [1, 2, 3, 4, 5, 500, 501, 502]
        impossible_pattern = [7777]

        pattern_type = "Default pattern"
        if pattern in so_rare_patterns:
            price *= 30
            pattern_type = "SOOO Rare Pattern"
        elif pattern in rare_patterns:
            price *= 3
            pattern_type = "Rare Pattern"
        elif pattern in impossible_pattern:
            price *= 0
            pattern_type = "Kill yourself, cheater, zxczxczxczxc"
        else:
            price *= 1

        if SkinClass.stattrack_can_be:
            chance_statrack = random.randint(0, 100)
            if target_case.chance_startrack > chance_statrack:
                is_statrack = True
                price *= 1.3

        price = round(price, 2)

        json_end_iteration = \
            {f"Case {i}" : {"SkinName" : SkinClass.name,
             "CaseName" : target_case.name,
             "rare" : SkinClass.rare,
             "price" : price,
             "stattrack" : is_statrack,
             "skin_float" : skin_float,
             "pattern" : pattern,
             "pattern_type" : pattern_type}}


        merged_end_answer = {**json_end_answer, **json_end_iteration}
        json_end_answer = merged_end_answer

    return JsonResponse(json_end_answer)


def help(request):
    return JsonResponse(
        {"Инструкция" : "Абсолютно лубой URL ведет на открытие кейса, кроме этого (/help)"
                         "Для открытия кейса прописывается 2 необязательных парамметра."
                         "Это count и id. Пример: cs2cases-site?count=10&id=CaseCS16"
                         "ID существует четыре - CaseCS16, CaseCSGO, CaseKilovat, CaseDangerZone"
                         "В каждом из них есть 4 предмета"})
