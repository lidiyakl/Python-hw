# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
import argparse

logging.basicConfig(filename='triangle.log',
                    encoding='utf-8',
                    format='{levelname:<7} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO,)
logger = logging.getLogger(__name__)


class TriangleError(Exception):
    pass


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_existence(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise TriangleError("Треугольник с такими сторонами не существует")

    def check_positive(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise TriangleError("Длина стороны не может быть неположительным числом")

    def get_type(self):
        if self.a == self.b and self.b == self.c:
            return "Равносторонний треугольник"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"


def main(a, b, c):
    try:
        triangle = Triangle(a, b, c)
        triangle.check_positive()
        triangle.check_existence()

        triangle_type = triangle.get_type()
        logger.info(triangle_type)
        print(triangle_type)

    except ValueError:
        logging.error("Ошибка: введены некорректные значения сторон")
        print("Ошибка: введены некорректные значения сторон")
    except TriangleError as e:
        logging.error(str(e))
        print("Ошибка:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Определение типа треугольника по длинам его сторон")
    parser.add_argument("a", type=float, help="Длина стороны a")
    parser.add_argument("b", type=float, help="Длина стороны b")
    parser.add_argument("c", type=float, help="Длина стороны c")
    args = parser.parse_args()

    try:
        main(args.a, args.b, args.c)
    except Exception as e:
        logging.error("Произошла ошибка: " + str(e))