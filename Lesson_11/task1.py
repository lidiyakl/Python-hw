# Задание 1. Создайте класс Матрица. Добавьте методы для:

# вывода на печать,
# сравнения,
# сложения,
# умножения матриц

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def fill(self, values):
        if len(values) != self.rows * self.columns:
            raise ValueError("Количество значений должно соответствовать размеру матрицы")
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = values[i * self.columns + j]

    def print(self):
        for row in self.data:
            print(" ".join(map(str, row)))

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __gt__(self, other):  # больше >
        return self.data > other.data

    def __ge__(self, other):  # больше или равно >=
        return self.data >= other.data

    def __lt__(self, other):  # метод меньше <
        return self.data < other.data

    def __le__(self, other):  # меньше или равно <=
        return self.data <= other.data

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Для сложения размеры матриц должны совпадать")

    def __mul__(self, other):
        if self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Число столбцов в первой матрице должно совпадать с числом строк во второй матрице")


# Пример использования класса Matrix
matrix1 = Matrix(2, 2)
matrix1.fill([1, 2, 3, 4])

matrix2 = Matrix(2, 2)
matrix2.fill([5, 6, 7, 8])

print("Матрица 1:")
matrix1.print()

print("Матрица 2:")
matrix2.print()

result_sum = matrix1 + matrix2
print("Сумма матриц:")
result_sum.print()

result_multiply = matrix1 * matrix2
print("Произведение матриц:")
result_multiply.print()

print("Сравнение матриц:")
print(matrix1 < matrix2)