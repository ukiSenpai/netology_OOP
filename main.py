class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sum_grades = 0
        count_grade = 0
        for grade in self.grades.values():
            for gredes in grade:
                count_grade += 1
                sum_grades += gredes
        mid_grade = sum_grades/count_grade
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

    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def __str__(self):
        sum_grades = 0
        count_grade = 0
        for grade in self.grades.values():
            for gredes in grade:
                count_grade += 1
                sum_grades += gredes
            mid_grade = sum_grades / count_grade
            res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(mid_grade,1)}'
        return res


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



#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python','Java']
#
# cool_lector = Lecturer('Emma','Kers')
# cool_lector.courses_attached += ['Python','Java']
#
# best_reviewer = Reviewer('Serg','Best')
#
# best_student.rate_lect(cool_lector,'Java',8)
# best_student.rate_lect(cool_lector,'Java',10)
# best_student.rate_lect(cool_lector,'Java',8)
# best_student.rate_lect(cool_lector,'Python',9)
# best_student.rate_lect(cool_lector,'Python',8)
# best_student.rate_lect(cool_lector,'Python',10)
#
# cool_reviewer = Reviewer('Some', 'Buddy')
# cool_reviewer.courses_attached += ['Python']
#
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
# print(cool_lector.grades)
# print(best_reviewer)
# print(cool_lector)
# print(best_student)


best_lecturer = Lecturer("Diana", "Best")
worse_lecturer = Lecturer("Nikola", "Worse")

best_lecturer.courses_attached += ['Python','Java']
worse_lecturer.courses_attached += ['Python','Java']

best_student = Student("Serg", "Best", "man")
worse_student = Student("Niki", "Worse", "woman")

reviewer_py = Reviewer("Lion", "Tex")
reviewer_java = Reviewer("Dave", "Rev")
reviewer_py.courses_attached += ['Python']
reviewer_java.courses_attached += ['Java']
reviewer_py.rate_hw(best_student, "Python", 10)
reviewer_py.rate_hw(worse_student, "Python", 10)
reviewer_java.rate_hw(best_student, "Java", 10)
reviewer_java.rate_hw(worse_student, "Java", 10)



best_student.courses_in_progress += ['Python','Java']
best_student.finished_courses += ['Git']
best_student.rate_lect(best_lecturer,"Python",10)
best_student.rate_lect(best_lecturer,"Java",9)
best_student.rate_lect(worse_lecturer,"Python",6)
best_student.rate_lect(worse_lecturer,"Java",7)


worse_student.courses_in_progress += ['Python','Java']
worse_student.finished_courses += ['Git']
worse_student.rate_lect(best_lecturer,"Python",9)
worse_student.rate_lect(best_lecturer,"Java",9)
worse_student.rate_lect(worse_lecturer,"Python",8)
worse_student.rate_lect(worse_lecturer,"Java",6)




print(worse_student)
print(best_student)
print(best_lecturer)
print(worse_lecturer)


