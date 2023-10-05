# Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. Функцию hex 
# используйте для проверки своего результата.



def hexadecimal_number(number):
    hex_number = ""
    if number != 0:
        while number > 0:
            remainder = number % 16
            match remainder:
                case 10:
                    hex_digit = "A"
                case 11:
                    hex_digit = "B"
                case 12:
                    hex_digit = "C"
                case 13:
                    hex_digit = "D"
                case 14:
                    hex_digit = "E"
                case 15:
                    hex_digit = "F"
                case _:
                    hex_digit = str(remainder)
            hex_number = hex_digit + hex_number
            number //= 16
    else:
        hex_number = "0"
    return "0x" + hex_number


decimal_number = int(input("Введите целое число: "))
print("Своя функция:", decimal_number, "->", hexadecimal_number(decimal_number))
print("Проверка функцией hex:", decimal_number, "->", hex(decimal_number))