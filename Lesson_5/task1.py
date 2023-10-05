# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.



def split_file_path(data: str):
    dir_name, file_name = data.rsplit("\\", 1)
    name, extension = file_name.split(".")
    return dir_name, name, extension


input_str = r"C:\Путь\к\файлу\Файл.py"
print(split_file_path(input_str))