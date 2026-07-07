from student import Student


class CourseGroup:
    def __init__(self, student: Student, classmates: list[Student]):
        self.student = student
        self.classmates = classmates
