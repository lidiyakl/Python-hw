# Создайте словарь со списком вещей для похода в качестве ключа и их массой 
# в качестве значения. Определите какие вещи влезут в рюкзак передав его 
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.


import itertools

things = {
    "Палатка": 2.5,
    "Спальник": 1.5,
    "Пенка": 0.5,
    "Еда": 1.0,
    "Перчатки": 0.2,
    "Фонарик": 0.3,
    "Котелок": 1.0,
    "Ботинки": 2.0,
    "Вода": 3.0
}

MAX_WEIGHT = 7.0


def all_combinations(items):
    all_combinations = []
    for i in range(1, len(items) + 1):
        combinations = itertools.combinations(items, i)
        all_combinations.extend(combinations)
    return all_combinations


def valid_combinations(list, max_weight):
    valid_combinations = []
    for combination in list:
        total_weight = sum(item[1] for item in combination)
        if total_weight <= max_weight:
            valid_combinations.append(combination)
    return valid_combinations


valid_combinations = valid_combinations(all_combinations(things.items()), MAX_WEIGHT)

for combination in valid_combinations:
    print("Вариант комплектации:")
    total_weight = 0
    for item in combination:
        total_weight = total_weight + item[1]
        print(f"{item[0]}")
    print(f"Общий вес: {total_weight}")
    print()