# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой 
# длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате 
# получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма 
# рассчитывается как ставка умноженная на процент премии


names_list = ["Иванов", "Петров", "Сидоров"]
salary_list = [10000, 15000, 20000]
bonus_list = ["10.25%", "15.20%", "5.0%"]

my_dict = {name: rate * float(percent.rstrip("%")) / 100
           for name, rate, percent in zip(names_list, salary_list, bonus_list)}

print(my_dict)