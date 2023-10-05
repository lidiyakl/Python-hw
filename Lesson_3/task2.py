# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки 
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

import re

text = """Одной из интересных синтаксических особенностей языка является выделение блоков кода с помощью отступов 
        (пробелов или табуляций), поэтому в Python отсутствуют операторные скобки begin/end, как в языке Паскаль, 
        или фигурные скобки, как в Си. Такой «трюк» позволяет сократить количество строк и символов в программе и 
        приучает к «хорошему» стилю программирования. С другой стороны, поведение и даже корректность программы 
        может зависеть от начальных пробелов в тексте. Тем, кто привык программировать на языках с явным выделением 
        начала и конца блоков, такое поведение поначалу может показаться неинтуитивным и неудобным."""


def list_without_punctuation(data):  # Возвращает список слов, без знаков препинания, пробелов и в нижнем регистре.
    result_list = re.sub(r'[^\w\s]', '', data.lower()).split()
    return result_list


def count_word(data):  # Возвращает количество встречаемых слов в тексте.
    dict_recurring_word = []
    for word in data:
        if word not in dict_recurring_word:
            dict_recurring_word.append(word)
    count_word = len(dict_recurring_word)
    return count_word


def recurring_word(data):  # Возвращает список повторяющихся слов.
    dict_recurring_word = []
    for word in data:
        dict_count_word = word, data.count(word),
        if data.count(word) > 1 and dict_count_word not in dict_recurring_word:
            dict_recurring_word.append(dict_count_word)
    return dict_recurring_word


def sort_recurring_word(data):  # Возвращает список отсортированных по убыванию повторяющихся слов.
    sort_recurring_word = dict(sorted(data, key=lambda x: x[1], reverse=True))
    frequency_word = []
    for key in sort_recurring_word.keys():
        frequency_word.append(key)
    return frequency_word


print(f'Количество встречающихся слов в тексте: {count_word(list_without_punctuation(text))}')
print(f'10 самых частых слов: {sort_recurring_word(recurring_word(list_without_punctuation(text)))[:10]}\n')