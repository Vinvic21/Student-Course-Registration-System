from services.school_system import SchoolSystem

def main():
    system = SchoolSystem()

    while True:
        print("Student Course Registration System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Register Student to Course")
        print("7. View Students in a Course")
        print("8. View Courses for a Student")
        print("9. Save Data")
        print("10. Load Data")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_ID = input("Enter student ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            try:
                system.add_student(student_ID, name, email, phone)
            except ValueError as Error:
                print(f"{Error}")

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            student_ID = input("Enter student ID to search: ")
            student = next((s for s in system.students if s["student_ID"] == student_ID), None)
            if student:
                print(f"{student['name']} ({student['email']}, {student['phone_number']})")
            else:
                print("Student doesnt exist.")

        elif choice == "4":
            course_ID = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            trainer_name = input("Enter trainer name: ")
            capacity = int(input("Enter capacity: "))
            try:
                system.add_course(course_ID, course_name, trainer_name, capacity)
            except ValueError as Error:
                print(f"{Error}")

        elif choice == "5":
            for course in system.courses:
                print(f"{course['course_ID']}: {course['course_name']} (Trainer: {course['trainer_name']}, Capacity: {course['capacity']}, Enrolled: {course.get('enrolled',0)})")

        elif choice == "6":
            student_ID = input("Enter student ID: ")
            course_ID = input("Enter course ID: ")
            system.register_student(student_ID, course_ID)

        elif choice == "7":
            course_ID = input("Enter course ID: ")
            students_in_course = [r["student_ID"] for r in system.registrations if r["course_ID"] == course_ID]
            if students_in_course:
                print("Students in course:")
                for sid in students_in_course:
                    student = next((s for s in system.students if s["student_ID"] == sid), None)
                    if student:
                        print(f" {student['name']} ({student['student_ID']})")
            else:
                print("No students registered in this course.")

        elif choice == "8":
            student_ID = input("Enter student ID: ")
            courses_for_student = [r["course_ID"] for r in system.registrations if r["student_ID"] == student_ID]
            if courses_for_student:
                print("Courses for student:")
                for cid in courses_for_student:
                    course = next((c for c in system.courses if c["course_ID"] == cid), None)
                    if course:
                        print(f"{course['course_name']} ({course['course_ID']})")
            else:
                print("No courses found for this student.")

        elif choice == "9":
            
            from services.school_system import write_file
            write_file("students.json", system.students)
            write_file("courses.json", system.courses)
            write_file("registrations.json", system.registrations)
            print("Data saved successfully.")

        elif choice == "10":
            
            from services.school_system import open_file
            system.students = open_file("students.json")
            system.courses = open_file("courses.json")
            system.registrations = open_file("registrations.json")
            print("Data loaded successfully.")

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
