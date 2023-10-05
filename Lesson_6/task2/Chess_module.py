from random import randint

# правильная расстановка ферзей (для тестирования)
_good_position = [[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]

# неправильная расстановка ферзей (для тестирования)
_bad_position = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]


def check_positions(pos):
    for i in range(8):
        for j in range(i + 1, 8):
            if (pos[i][0] == pos[j][0] or pos[i][1] == pos[j][1] or
                    abs(pos[i][0] - pos[j][0]) == abs(pos[i][1] - pos[j][1])):
                return False
    return True


def generate_position():
    return [[randint(0, 7), randint(0, 7)] for _ in range(0, 8)]


def find_position():
    count = 0
    while count < 4:
        pos = generate_position()
        if check_positions(pos):
            print(f'Успешная расстановка: {pos}')
            count += 1


if __name__ == '__main__':
    print(check_positions(_good_position))
    print(check_positions(_bad_position))
    print(generate_position())