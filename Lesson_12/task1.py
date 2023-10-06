# Создайте класс студента.

# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы 
# в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам 
# всех предметов вместе взятых.

import csv


class NameValidator:
    def __get__(self, instance, owner):
        return instance._fio

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("ФИО должно быть строкой")
        if not value.replace(" ", "").isalpha():
            raise ValueError("ФИО должно содержать только буквы")
        if not value.istitle():
            raise ValueError("ФИО должно начинаться с заглавной буквы")
        instance._fio = value


class Validator:
    @staticmethod
    def check_subject(subject, valid_subjects):
        if subject not in valid_subjects:
            raise ValueError(f"Предмет {subject} недопустим")

    @staticmethod
    def check_mark(mark):
        if mark < 2 or mark > 5:
            raise ValueError("Оценка должна быть от 2 до 5")

    @staticmethod
    def check_test_result(result):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")


class Student:
    fio = NameValidator()

    def __init__(self, fio, subjects_file):
        self.fio = fio
        self.subjects = self._load_subjects(subjects_file)
        self.grades = {subject: {'marks': [], 'test_results': []} for subject in self.subjects}

    @staticmethod
    def _load_subjects(subjects_file):
        subjects = []
        with open(subjects_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                subjects.append(row[0])
        return subjects

    def add_grade(self, subject, mark, test_result):
        Validator.check_subject(subject, self.subjects)
        Validator.check_mark(mark)
        Validator.check_test_result(test_result)

        self.grades[subject]['marks'].append(mark)
        self.grades[subject]['test_results'].append(test_result)

    def calculate_average_marks(self):
        total_marks = []
        print(self.fio)
        for subject in self.subjects:
            marks = self.grades[subject]['marks']
            total_marks.extend(marks)
            if marks:
                average_mark = sum(marks) / len(marks)
                print(f"Средний балл по предмету {subject}: {average_mark:.2f}")

        if total_marks:
            average_total_mark = sum(total_marks) / len(total_marks)
            print(f"Средний балл по всем предметам: {average_total_mark:.2f}")

    def calculate_average_test_score(self):
        for subject in self.subjects:
            scores = self.grades[subject]['test_results']
            if scores:
                average_score = sum(scores)/len(scores)
                print(f"Средний балл по тестам по предмету {subject}: {average_score:.2f}")

    def overall_average_grade(self):
        total_marks = []
        for subject in self.subjects:
            marks = self.grades[subject]['marks']
            total_marks.extend(marks)
        if total_marks:
            average_total_mark = sum(total_marks) / len(total_marks)
            print(f"Средняя оценка по всем предметам: {average_total_mark:.2f}")


student1 = Student('Иванов Иван Иванович', 'subjects.csv')
student1.add_grade('Математика', 4, 80)
student1.add_grade('Физика', 2, 30)
student1.add_grade('История', 3, 70)
student1.add_grade('Математика', 5, 100)

student2 = Student('Петров Петр Петрович ', 'subjects.csv')
student2.add_grade('Математика', 3, 60)
student2.add_grade('Литература', 5, 100)
student2.add_grade('История', 4, 75)
student2.add_grade('Физика', 3, 50)

print(f'Студент {student1.fio}:')
student1.calculate_average_test_score()
student1.overall_average_grade()

print(f'Студент {student2.fio}:')
student2.calculate_average_test_score()
student2.overall_average_grade()