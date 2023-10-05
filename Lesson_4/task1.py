# Напишите функцию для транспонирования матрицы


def transpose_matrix(data: list):
    """Функция транспонирования матрицы."""
    trans_matrix = []
    for _ in range(0, len(data[0])):
        trans_matrix.append([])
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            trans_matrix[j].append(data[i][j])
    return trans_matrix


def print_matrix(data: list):
    """Функция вывода матрицы."""
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            print(f"{data[i][j]} ", end="")
        print()


my_matrix = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]

print("Исходная матрица:")
print_matrix(my_matrix)

print("Транспонированная матрица:")
print_matrix(transpose_matrix(my_matrix))