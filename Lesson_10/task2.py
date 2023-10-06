"""
Задача 2
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""

import fractions


class FractionCalculator:
    def __init__(self):
        self.num1 = 0
        self.den1 = 1
        self.num2 = 0
        self.den2 = 1

    def set_fractions(self, fraction_str1, fraction_str2):
        try:
            self.num1, self.den1 = map(int, fraction_str1.split('/'))
            self.num2, self.den2 = map(int, fraction_str2.split('/'))
        except ValueError:
            print("Неверный формат. Введите дробь в формате a/b")

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def sum_of_fractions(self):
        if self.den1 == self.den2:
            sum_numerator = self.num1 + self.num2
            common_den = self.den1
        else:
            sum_numerator = (self.num1 * self.den2) + (self.num2 * self.den1)
            common_den = self.den1 * self.den2
        common_divisor = self.gcd(common_den, sum_numerator)
        final_numerator = sum_numerator // common_divisor
        final_den = common_den // common_divisor
        return final_numerator, final_den

    def product_of_fractions(self):
        product_numerator = self.num1 * self.num2
        common_den = self.den1 * self.den2
        common_divisor = self.gcd(common_den, product_numerator)
        final_numerator = product_numerator // common_divisor
        final_den = common_den // common_divisor
        return final_numerator, final_den


if __name__ == "__main__":
    calculator = FractionCalculator()

    fraction_str1 = input("Введите первую дробь в формате a/b: ")
    fraction_str2 = input("Введите вторую дробь в формате a/b: ")

    calculator.set_fractions(fraction_str1, fraction_str2)

    result_sum = calculator.sum_of_fractions()
    result_product = calculator.product_of_fractions()

    print(f'Сумма дробей: {result_sum[0]}/{result_sum[1]}')
    print(f'Произведение дробей: {result_product[0]}/{result_product[1]}')

    print()
    print('Проверка с помощью модуля fractions')
    fraction_1 = fractions.Fraction(calculator.num1, calculator.den1)
    fraction_2 = fractions.Fraction(calculator.num2, calculator.den2)
    print(f'Сумма дробей: {fraction_1 + fraction_2}')
    print(f'Произведение дробей: {fraction_1 * fraction_2}')