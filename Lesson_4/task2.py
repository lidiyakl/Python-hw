# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.

def key_to_value(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            my_dict[value] = key
        except TypeError:
            my_dict[str(value)] = key
    return my_dict


print(key_to_value(name='Vladimir', profession='student', age=37, city='Moscow', hobbies=['hockey', 'football']))