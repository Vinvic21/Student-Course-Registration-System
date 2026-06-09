from models.student import Student
from models.course import Course
import os
import json

DATA_FILES = "data"

def open_file(filename):
    path = os.path.join(DATA_FILES, filename)
    if not os.path.exists(path):
        return []
    with open(path, "r") as file:
        return json.load(file)

def write_file(filename, data):
    path = os.path.join(DATA_FILES, filename)
    with open(path, "w") as file:
        json.dump(data, file)

class SchoolSystem:
    def __init__(self):
        self.students = open_file("students.json")
        self.courses = open_file("courses.json")
        self.registrations = open_file("registration.json")
        
    def add_student(self, student_ID, name, email, phone_number):
        for student in self.students:
            if student["student_ID"] == student_ID:
                raise ValueError("Student already exist")
        new_student = {
            "student_ID": student_ID,
            "name": name,
            "email": email,
            "phone_number": phone_number
        }
        self.students.append(new_student)
        print(f"{new_student['name']} added to the list")
        
    def add_course(self, course_ID, course_name, trainer_name, capacity):
        for course in self.courses:
            if course["course_ID"] == course_ID:
                raise ValueError("Course already exist")
        new_course = {
            "course_ID": course_ID,
            "course_name": course_name,
            "trainer_name": trainer_name,
            "capacity": capacity,
            "enrolled": 0
        }
        self.courses.append(new_course)
        print(f"{new_course['course_name']} added to the list")
        
    def register_student(self, student_ID, course_ID):
        student = next((s for s in self.students if s["student_ID"] == student_ID), None)
        course = next((c for c in self.courses if c["course_ID"] == course_ID), None)

        if not student:
            print("No student found")
            return
        if not course:
            print("No course found")
            return

        if course["enrolled"] >= course["capacity"]:
            print("Course capacity full")
            return

        course["enrolled"] += 1
        new_registration = {
            "student_ID": student_ID, 
            "course_ID": course_ID
        }
        self.registrations.append(new_registration)
        print(f"{student['name']} registered in {course['course_name']}.")

        write_file("courses.json", self.courses)
        write_file("registrations.json", self.registrations)

    def view_students(self):
        if not self.students:
            print("ℹ No students available.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f" - {student['student_ID']}: {student['name']} ({student['email']}, {student['phone_number']})")
