class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.courses = {}

    def add_course_mark(self, course_id, mark):
        self.courses[course_id] = mark
