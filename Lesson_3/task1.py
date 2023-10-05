# Дан список повторяющихся элементов. Вернуть список с дублирующимися 
# . В результирующем списке не должно быть дубликатов.



my_list = [1, 4, 2, 44, 1, 26, 3, 3, 1, 44, 87]

new_list = []
for el in my_list:
    if my_list.count(el) > 1 and new_list.count(el) == 0:
        new_list.append(el)
print(my_list)
print(new_list)