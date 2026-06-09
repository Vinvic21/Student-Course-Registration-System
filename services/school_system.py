from models.student import Student
from models.course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []
        self.registered = 0

    def add_student(self,student_ID, name, email, phone_number ):
        if self.registered >= self.capacity:
            raise ValueError("Course allready full")
        self.registered += 1
        for student in self.students:
            if student.student_ID == student_ID:
                raise ValueError("Student already exist")
            new_student = Student(student_ID, name, email, phone_number)
            self.students.append(new_student)
            print(f"{new_student.name} added to the list")
        

    def add_course(self,course_ID, course_name, trainer_name, capacity):
        for course in self.courses:
            if course.course_ID == course_ID:
                raise ValueError("Course already exist")
            new_course = Course(course_ID, course_name, trainer_name, capacity)
            self.courses.append(new_course)
            print(f"{new_course.course_name} added to the list")
        

    def register_student(self):
        pass


    def view_students(self):
        pass
