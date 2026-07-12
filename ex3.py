from student import Student
from course import CourseGroup

student = Student("Оля", "Баранкина", 17, 3)

classmate1 = Student("Петя", "Петров", 18, 3)
classmate2 = Student("Катя", "Петрова", 17, 3)
classmate3 = Student("Света", "Лясина", 17, 3)

new_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(
    f"{new_group.student.name} "
    f"{new_group.student.surname}, "
    f"{new_group.student.age} лет, "
    f"учится на {new_group.student.course} курсе вместе с:"
)

for classmate in new_group.classmates:
    print(
        f"{classmate.name}, "
        f"{classmate.surname}, "
        f"{classmate.age}, "
        f"{classmate.course}")
