# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с 
# учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def traverse_directory(directory):
    data = []

    for root, dirs, files in os.walk(directory):
        total_size = sum(
            os.path.getsize(os.path.join(root, file)) for file in files
        )

        dir_info = {
            'name': os.path.basename(root),
            'path': os.path.relpath(root, directory),
            'type': 'directory',
            'size': total_size,
        }

        data.append(dir_info)

        for file in files:
            file_info = {
                'name': os.path.basename(file),
                'path': os.path.relpath(root, directory),
                'type': 'file',
                'size': os.path.getsize(os.path.join(root, file)),
            }

            data.append(file_info)

    # Сохранение результатов в JSON, CSV и Pickle
    with open('result.json', 'w') as json_file:
        json.dump(data, json_file)

    # Сохранение результатов в CSV
    with open('result.csv', 'w', newline='') as csv_file:
        fieldnames = ['name', 'path', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    # Сохранение результатов в Pickle
    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


traverse_directory(".")