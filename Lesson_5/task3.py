# Создайте функцию генератор чисел Фибоначчи


def gen_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


number_fib = gen_fibonacci()
for _ in range(15):
    number = next(number_fib)
    print(number, end=' ')