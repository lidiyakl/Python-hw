# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода используйте 
# модуль fractions.



import fractions


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sum_of_divisors(num1, den1, num2, den2):
    if den1 == den2:
        sum_numerator = num1 + num2
        common_den = den1
    else:
        sum_numerator = (num1 * den2) + (num2 * den1)
        common_den = den1 * den2
    common_divisor = gcd(common_den, sum_numerator)
    final_numerator = sum_numerator // common_divisor
    final_den = common_den // common_divisor
    return print(f'Сумма дробей: {str(final_numerator)}/{str(final_den)}')


def product_of_divisors(num1, den1, num2, den2):
    product_numerator = num1 * num2
    common_den = den1 * den2
    common_divisor = gcd(common_den, product_numerator)
    final_numerator = product_numerator // common_divisor
    final_den = common_den // common_divisor
    return print(f'Произведение дробей: {str(final_numerator)}/{str(final_den)}')


fraction_str1 = input("Введите первую дробь в формате a/b: ")
fraction_str2 = input("Введите вторую дробь в формате a/b: ")
num1, den1 = map(int, fraction_str1.split('/'))
num2, den2 = map(int, fraction_str2.split('/'))

sum_of_divisors(num1, den1, num2, den2)
product_of_divisors(num1, den1, num2, den2)

print()
print('Проверка с помощью модуля fractions')
fraction_1 = fractions.Fraction(num1, den1)
fraction_2 = fractions.Fraction(num2, den2)
print(f'Сумма дробей: {fraction_1 + fraction_2}')
print(f'Произведение дробей: {fraction_1 * fraction_2}')