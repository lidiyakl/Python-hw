# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого 
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше 
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить 
# является ли треугольник разносторонним, равнобедренным или равносторонним.


a, b, c = map(float, input("Введите длины сторон треугольника через пробел: ").split())


def check_triangle(side_a, side_b, side_c):
    if side_a + side_b > side_c or side_a + side_c > side_b or side_b + side_c > side_a:
        return True
    else:
        return False


def triangle_type(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return "Треугольник равносторонний"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"


if check_triangle(a, b, c):
    print(triangle_type(a, b, c))
else:
    print("Треугольник не существует")