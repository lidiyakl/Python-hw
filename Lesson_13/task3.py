# Задача 3 Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны 
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то 
# треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
# равнобедренным или равносторонним.


class TriangleError(Exception):
    pass


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise TriangleError("Треугольник с такими сторонами не существует")

    def check_positive(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise TriangleError("Длина стороны должна быть больше 0")

    def triangle_type(self):
        if self.a == self.b and self.b == self.c:
            return "Треугольник равносторонний "
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Треугольник равнобедренный "
        else:
            return "Треугольник разносторонний "


# Пример использования
try:
    a, b, c = map(float, input("Введите длины сторон треугольника через пробел: ").split())

    triangle = Triangle(a, b, c)
    triangle.check_positive()
    triangle.check_triangle()

    triangle_type = triangle.triangle_type()
    print(triangle_type)

except ValueError:
    print("Ошибка: введены некорректные значения сторон")
except TriangleError as e:
    print("Ошибка:", e)