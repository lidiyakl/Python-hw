# Задача 1
# Доработаем задания 5-6.Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и 
# параметры для этого типа. Внутри класса создайте экземпляр на основе 
# переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fish(Animal):
    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Bird(Animal):
    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammal(Animal):
    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


# Класс-фабрика
class AnimalFactory:
    animal_types = {
        "Fish": Fish,
        "Bird": Bird,
        "Mammal": Mammal
    }

    @staticmethod
    def create_animal(animal_type, kind, name, age, specific_param):
        if animal_type in AnimalFactory.animal_types:
            animal_class = AnimalFactory.animal_types[animal_type]
            return animal_class(kind, name, age, specific_param)
        else:
            raise ValueError(f"Unsupported animal type: {animal_type}")


# Пример использования класса-фабрики
fish = AnimalFactory.create_animal("Fish", "Fish", "Nemo", 2, "Small")
bird = AnimalFactory.create_animal("Bird", "Bird", "Robin", 1, "Red")
mammal = AnimalFactory.create_animal("Mammal", "Mammal", "Lion", 5, "Wild")

# Вывод информации о созданных животных
print(f"{fish.get_kind()} {fish.get_name()} is {fish.get_age()} years old and is {fish.get_specific()} in size.")
print(f"{bird.get_kind()} {bird.get_name()} is {bird.get_age()} years old and is {bird.get_specific()} in color.")
print(f"{mammal.get_kind()} {mammal.get_name()} is {mammal.get_age()} years old and is {mammal.get_specific()}.")