import cmath
import json
import functools
import csv
import random
import os

# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

def save_to_json(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            data = {
                "function": func.__name__,
                "arguments": args,
                "keyword_arguments": kwargs,
                "result": [str(x) for x in result]
            }

            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            return result
        return wrapper
    return decorator

def find_roots(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

def generate_csv(filename, rows=100):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            writer.writerow([random.randint(-100, 100) for _ in range(3)])

def apply_to_csv(csv_filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            with open(csv_filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    a, b, c = map(int, row)
                    results.append(func(a, b, c, *args, **kwargs))
            return results
        return wrapper
    return decorator

@save_to_json('roots_result.json')
@apply_to_csv('random_numbers.csv')
def find_and_save_roots(a, b, c):
    return find_roots(a, b, c)

generate_csv('random_numbers.csv', rows=100)
find_and_save_roots()