class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        amount = 0
        quantity = 0
        for num in self.grades.values():
            amount += sum(num)
            quantity += len(num)
        res = round(amount / quantity, 2)
        return res

    def avg_rate_course(self, course):
        amount_crs = 0
        quantity_crs = 0
        for num in self.grades.keys():
            if num == course:
                amount_crs += sum(self.grades[course])
                quantity_crs += len(self.grades[course])
        res = round(amount_crs / quantity_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории сравниваем.")
            return
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        amount = 0
        quantity = 0
        for num in self.grades.values():
            amount += sum(num)
            quantity += len(num)
        res = round(amount / quantity, 2)
        return res

    def avg_rate_course(self, course):
        amount_crs = 0
        quantity_crs = 0
        for num in self.grades.keys():
            if num == course:
                amount_crs += sum(self.grades[course])
                quantity_crs += len(self.grades[course])
        res = round(amount_crs / quantity_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Разные категории не сравниваем.")
            return
        return self.average_rating() < other.average_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


student_1 = Student('Юрий', 'Петров', 'Муж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Git"]

student_2 = Student('Анна', 'Иванова', 'Жен')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Git"]

lecturer_1 = Lecturer('Семён', 'Булыгин')
lecturer_2 = Lecturer('Мария', 'Кузикова')

reviewer_1 = Reviewer('Иван', 'Сидоров')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Сергей', 'Комаров')
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)

student_1.rate_hw(lecturer_1, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Python', 4)
student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Python', 5)

student_list = [student_1, student_2]
lector_list = [lecturer_1, lecturer_2]

import gc

print("Ревьюэры:")
print()
for obj in gc.get_objects():
    if isinstance(obj, Reviewer):
        print(obj)

print("Лекторы:")
print()
for obj in gc.get_objects():
    if isinstance(obj, Lecturer):
        print(obj)

print("Студенты:")
print()
for obj in gc.get_objects():
    if isinstance(obj, Student):
        print(obj)

print('Сравнение по средним оценкам:')
print()

if student_1 > student_2:
    print(f'{student_1.name} учится лучше чем {student_2.name}')
else:
    print(f'{student_2.name} учится лучше чем {student_1.name}')

if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} преподает лучше чем {lecturer_2.name}')
else:
    print(f'{lecturer_2.name} преподает лучше чем {lecturer_1.name}')
print()


def avg_rate_course_std(course, student_list):
    amount = 0
    quantity = 0
    for std in student_list:
        for num in std.grades:
            std_sum_rate = std.avg_rate_course(course)
            amount += std_sum_rate
            quantity += 1
    res = round(amount / quantity, 2)
    return res


def avg_rate_course_lct(course, lector_list):
    amount = 0
    quantity = 0
    for lct in lector_list:
        for num in lct.grades:
            lct_sum_rate = lct.avg_rate_course(course)
            amount += lct_sum_rate
            quantity += 1
    res = round(amount / quantity, 2)
    return res

print('Средняя оценка за домашние задания:')
print(avg_rate_course_std('Python', student_list))

print('Средняя оценка за лекции:')
print(avg_rate_course_lct('Python', lector_list))


