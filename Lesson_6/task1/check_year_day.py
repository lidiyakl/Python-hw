"""Модуль для проверки даты"""


def check_date(date):
    """Функция для проверки даты"""
    day, month, year = map(int, date.split('.'))
    if (year < 1 or year > 9999 or
            month < 1 or month > 12 or
            day < 1 or day > 31):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month in [2] and day > 29 and not leap_year(year):
        return False
    return True


def leap_year(year):
    """Функция для проверки высокосного года"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False