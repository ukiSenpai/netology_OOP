class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __eq__(self, other):
        one_grade = [sum_grade for one_cycle in self.grades.values() for sum_grade in one_cycle]
        second_grade = [sum_grade for one_cycle in other.grades.values() for sum_grade in one_cycle]
        if (sum(one_grade) / len(one_grade)) == (sum(second_grade) / len(second_grade)):
            return f"Оценки у {self.name} и {other.name} равны"
        else:
            return f"Оценки у {self.name} и {other.name} не равны "

    def __lt__(self, other):
        one_grade = [sum_grade for one_cycle in self.grades.values() for sum_grade in one_cycle]
        second_grade = [sum_grade for one_cycle in other.grades.values() for sum_grade in one_cycle]
        if (sum(one_grade) / len(one_grade)) < (sum(second_grade) / len(second_grade)):
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)}" \
                   f" ниже чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"
        else:
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)} " \
                   f"выше чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"


    def __gt__(self, other):
        one_grade = [sum_grade for one_cycle in self.grades.values() for sum_grade in one_cycle]
        second_grade = [sum_grade for one_cycle in other.grades.values() for sum_grade in one_cycle]
        if (sum(one_grade) / len(one_grade)) > (sum(second_grade) / len(second_grade)):
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)} " \
                   f"выше чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"
        else:
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)} " \
                   f"ниже чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"

    def __str__(self):
        sum_grades = []
        for grade in self.grades.values():
            for gredes in grade:
                sum_grades += [gredes]
        mid_grade = sum(sum_grades) / len(sum_grades)
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname} ' \
              f'\nСредняя оценка за домашние задания: {round(mid_grade, 1)} ' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} ' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        sum_grades = []
        for grade in self.grades.values():
            for gredes in grade:
                sum_grades += [gredes]
        mid_grade = sum(sum_grades) / len(sum_grades)
        res = f'Имя: {self.name} \nФамилия: {self.surname} ' \
            f'\nСредняя оценка за лекции: {round(mid_grade, 1)}'
        return res

    def __eq__(self, other):
        one_grade = [sum_grade for one_cycle in self.grades.values() for sum_grade in one_cycle]
        second_grade = [sum_grade for one_cycle in other.grades.values() for sum_grade in one_cycle]
        if (sum(one_grade) / len(one_grade)) == (sum(second_grade) / len(second_grade)):
            return f"Оценки у {self.name} и {other.name} равны"
        else:
            return f"Оценки у {self.name} и {other.name} не равны "

    def __lt__(self, other):
        one_grade = [sum_grade for one_cycle in self.grades.values() for sum_grade in one_cycle]
        second_grade = [sum_grade for one_cycle in other.grades.values() for sum_grade in one_cycle]
        if (sum(one_grade) / len(one_grade)) < (sum(second_grade) / len(second_grade)):
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)}" \
                   f" ниже чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"
        else:
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)} " \
                   f"выше чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"

    def __gt__(self, other):
        one_grade = [sum_grade for one_cycle in self.grades.values() for sum_grade in one_cycle]
        second_grade = [sum_grade for one_cycle in other.grades.values() for sum_grade in one_cycle]
        if (sum(one_grade) / len(one_grade)) > (sum(second_grade) / len(second_grade)):
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)} " \
                   f"выше чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"
        else:
            return f"Оценки у {self.name} со средним баллом  {sum(one_grade) / len(one_grade)} " \
                   f"ниже чем у {other.name} со средним балом {sum(second_grade) / len(second_grade)}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



best_student = Student("Serg", "Best", "man")
worse_student = Student("Niki", "Worse", "woman")
best_student.courses_in_progress += ['Python', 'Java']
worse_student.courses_in_progress += ['Python', 'Java']
best_student.finished_courses += ['Git']
worse_student.finished_courses += ['Git']

best_lecturer = Lecturer("Diana", "Best")
worse_lecturer = Lecturer("Nikola", "Worse")
best_lecturer.courses_attached += ['Python', 'Java']
worse_lecturer.courses_attached += ['Python', 'Java']

reviewer_py = Reviewer("Lion", "Tex")
reviewer_java = Reviewer("Dave", "Rev")
reviewer_py.courses_attached += ['Python']
reviewer_java.courses_attached += ['Java']

best_student.rate_lect(best_lecturer, 'Python', 10)
best_student.rate_lect(best_lecturer, 'Java', 9)
best_student.rate_lect(worse_lecturer, 'Python', 6)
best_student.rate_lect(worse_lecturer, 'Java', 7)

worse_student.rate_lect(best_lecturer, 'Python', 9)
worse_student.rate_lect(best_lecturer, 'Java', 9)
worse_student.rate_lect(worse_lecturer, 'Python', 8)
worse_student.rate_lect(worse_lecturer, 'Java', 6)


reviewer_py.rate_hw(best_student, 'Python', 10)
reviewer_py.rate_hw(worse_student, 'Python', 8)
reviewer_java.rate_hw(best_student, 'Java', 10)
reviewer_java.rate_hw(worse_student, 'Java', 7)
reviewer_py.rate_hw(best_student, 'Python', 9)
reviewer_py.rate_hw(worse_student, 'Python', 10)
reviewer_java.rate_hw(best_student, 'Java', 9)
reviewer_java.rate_hw(worse_student, 'Java', 9)






print(best_lecturer)
print("_____________________")
print(worse_lecturer)
print("_____________________")
print(best_student)
print("_____________________")
print(worse_student)
print("_____________________")
print(reviewer_py)
print("_____________________")
print(reviewer_java)
print("_____________________")


studens = [best_student, worse_student]
lecturers = [best_lecturer, worse_lecturer]

def mid_grade_students(students,course_search):
    sum_grade = []
    for student in students:
        for course,grade in student.grades.items():
            if course_search in course:
                sum_grade += grade
    print(f"Средняя оценка у студентов за курс {course_search}: {sum(sum_grade) / len(sum_grade)}")

def mid_grade_lecturers(lecturers,course_search):
    sum_grade = []
    for lecturer in lecturers:
        for course,grade in lecturer.grades.items():
            if course_search in course:
                sum_grade += grade
    print(f"Средняя оценка у лекторов за курс {course_search}: {sum(sum_grade) / len(sum_grade)}")

mid_grade_students(studens,"Java")
mid_grade_students(studens,"Python")
print("_____________________")
mid_grade_lecturers(lecturers,"Java")
mid_grade_lecturers(lecturers,"Python")
print("_____________________")
print(best_student == worse_student)
print(best_student < worse_student)
print(best_student > worse_student)
print(worse_student < best_student)
print(worse_student > best_student)
print("_____________________")
print(best_lecturer == worse_lecturer)
print(best_lecturer < worse_lecturer)
print(best_lecturer > worse_lecturer)
print(worse_lecturer < best_lecturer)
print(worse_lecturer > best_lecturer)




