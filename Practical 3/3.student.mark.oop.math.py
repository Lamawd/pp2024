import math
import numpy as np
import curses

def student_number(stdscr):
    stdscr.addstr("Input number of students in a class: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def student_info(stdscr):
    stdscr.addstr("Enter ID: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()
    stdscr.addstr("Name: ")
    stdscr.refresh()
    name = stdscr.getstr().decode()
    stdscr.addstr("Date of birth: ")
    stdscr.refresh()
    dob = stdscr.getstr().decode()
    return {'ID': student_id,
            'Name': name,
            'DOB': dob,
            'Courses': {}}

def course_number(stdscr):
    stdscr.addstr("Please choose how many courses you want to add: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def course_info(stdscr):
    stdscr.addstr("ID: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    stdscr.addstr("Name: ")
    stdscr.refresh()
    name = stdscr.getstr().decode()
    return {'ID': course_id,
            'Name': name}

def input_student_marks(stdscr, students, courses):
    list_students(stdscr, students)
    stdscr.addstr("Enter the student ID for marks: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()

    if student_id in students:
        list_courses(stdscr, courses)
        stdscr.addstr("Select a course ID: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()

        if course_id in courses:
            stdscr.addstr("Enter mark for the selected course: ")
            stdscr.refresh()
            mark = float(stdscr.getstr().decode())
            # Round-down the mark to 1-digit decimal using floor function
            mark = math.floor(mark * 10) / 10
            students[student_id]['Courses'][course_id] = mark
            stdscr.addstr(f"Mark {mark} recorded for Student ID {student_id} in Course ID {course_id}.")
            stdscr.refresh()
        else:
            stdscr.addstr("Invalid course ID. Please try again.")
            stdscr.refresh()
    else:
        stdscr.addstr("Invalid student ID. Please try again.")
        stdscr.refresh()

def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("\nList of Students:")
    for student_id, student_info in students.items():
        stdscr.addstr(f"\nStudent ID: {student_id}, Name: {student_info['Name']}, DOB: {student_info['DOB']}")
    stdscr.refresh()

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("\nList of Courses:")
    for course_id, course_info in courses.items():
        stdscr.addstr(f"\nCourse ID: {course_id}, Name: {course_info['Name']}")
    stdscr.refresh()

def show_student_marks(stdscr, students):
    list_students(stdscr, students)
    stdscr.addstr("\nEnter the student ID to show marks: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()

    if student_id in students:
        stdscr.addstr(f"\nMarks for Student ID {student_id}:")
        for course_id, mark in students[student_id]['Courses'].items():
            stdscr.addstr(f"\nCourse ID: {course_id}, Mark: {mark}")
        stdscr.refresh()
    else:
        stdscr.addstr("Invalid student ID. Please try again.")
        stdscr.refresh()

def calculate_gpa(student, courses):
    credits = np.array([courses[course_id]['Credit'] for course_id in student['Courses']])
    marks = np.array([student['Courses'][course_id] for course_id in student['Courses']])
    weighted_sum = np.sum(credits * marks)
    total_credits = np.sum(credits)
    if total_credits == 0:
        return 0
    else:
        return weighted_sum / total_credits

def sort_students_by_gpa(students, courses):
    return sorted(students.values(), key=lambda x: calculate_gpa(x, courses), reverse=True)

def main(stdscr):
    students = {}
    courses = {}

    num_students = student_number(stdscr)
    for _ in range(num_students):
        student_info_data = student_info(stdscr)
        students[student_info_data['ID']] = student_info_data

    num_courses = course_number(stdscr)
    for _ in range(num_courses):
        course_info_data = course_info(stdscr)
        courses[course_info_data['ID']] = course_info_data
        # Adding a credit attribute to each course
        stdscr.addstr(f"Enter credit for course {course_info_data['ID']}: ")
        stdscr.refresh()
        courses[course_info_data['ID']]['Credit'] = int(stdscr.getstr().decode())

    while True:
        stdscr.clear()
        stdscr.addstr("Options:\n")
        stdscr.addstr("1. Input student marks for a course\n")
        stdscr.addstr("2. List courses\n")
        stdscr.addstr("3. List students\n")
        stdscr.addstr("4. Show student marks for a given course\n")
        stdscr.addstr("5. Calculate and display GPA for a student\n")
        stdscr.addstr("6. Sort students by GPA descending\n")
        stdscr.addstr("7. Exit\n")

        choice = stdscr.getch()

        if choice == ord('1'):
            input_student_marks(stdscr, students, courses)
        elif choice == ord('2'):
            list_courses(stdscr, courses)
        elif choice == ord('3'):
            list_students(stdscr, students)
        elif choice == ord('4'):
            show_student_marks(stdscr, students)
        elif choice == ord('5'):
            list_students(stdscr, students)
            stdscr.addstr("Enter the student ID to calculate GPA: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode()
            if student_id in students:
                gpa = calculate_gpa(students[student_id], courses)
                stdscr.addstr(f"GPA for Student ID {student_id}: {gpa:.2f}")
                stdscr.refresh()
            else:
                stdscr.addstr("Invalid student ID. Please try again.")
                stdscr.refresh()
        elif choice == ord('6'):
            sorted_students = sort_students_by_gpa(students, courses)
            stdscr.addstr("\nStudents sorted by GPA (descending):")
            for student in sorted_students:
                stdscr.addstr(f"\nStudent ID: {student['ID']}, Name: {student['Name']}, GPA: {calculate_gpa(student, courses):.2f}")
            stdscr.refresh()
        elif choice == ord('7'):
            stdscr.addstr("Exiting the program.")
            stdscr.refresh()
            break
        else:
            stdscr.addstr("You know this is not your right.\n")
            stdscr.refresh()

curses.wrapper(main)
import math
import curses

def student_number(stdscr):
    stdscr.addstr("Input number of students in a class: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def student_info(stdscr):
    stdscr.addstr("Enter ID: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()
    stdscr.addstr("Name: ")
    stdscr.refresh()
    name = stdscr.getstr().decode()
    stdscr.addstr("Date of birth: ")
    stdscr.refresh()
    dob = stdscr.getstr().decode()
    return {'ID': student_id,
            'Name': name,
            'DOB': dob,
            'Courses': {}}

def course_number(stdscr):
    stdscr.addstr("Please choose how many courses you want to add: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode())

def course_info(stdscr):
    stdscr.addstr("ID: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    stdscr.addstr("Name: ")
    stdscr.refresh()
    name = stdscr.getstr().decode()
    return {'ID': course_id,
            'Name': name}

def input_student_marks(stdscr, students, courses):
    list_students(stdscr, students)
    stdscr.addstr("Enter the student ID for marks: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()

    if student_id in students:
        list_courses(stdscr, courses)
        stdscr.addstr("Select a course ID: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()

        if course_id in courses:
            stdscr.addstr("Enter mark for the selected course: ")
            stdscr.refresh()
            mark = float(stdscr.getstr().decode())
            # Round-down the mark to 1-digit decimal using floor function
            mark = math.floor(mark * 10) / 10
            students[student_id]['Courses'][course_id] = mark
            stdscr.addstr(f"Mark {mark} recorded for Student ID {student_id} in Course ID {course_id}.")
            stdscr.refresh()
        else:
            stdscr.addstr("Invalid course ID. Please try again.")
            stdscr.refresh()
    else:
        stdscr.addstr("Invalid student ID. Please try again.")
        stdscr.refresh()

def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("\nList of Students:")
    for student_id, student_info in students.items():
        stdscr.addstr(f"\nStudent ID: {student_id}, Name: {student_info['Name']}, DOB: {student_info['DOB']}")
    stdscr.refresh()

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("\nList of Courses:")
    for course_id, course_info in courses.items():
        stdscr.addstr(f"\nCourse ID: {course_id}, Name: {course_info['Name']}")
    stdscr.refresh()

def show_student_marks(stdscr, students):
    list_students(stdscr, students)
    stdscr.addstr("\nEnter the student ID to show marks: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()

    if student_id in students:
        stdscr.addstr(f"\nMarks for Student ID {student_id}:")
        for course_id, mark in students[student_id]['Courses'].items():
            stdscr.addstr(f"\nCourse ID: {course_id}, Mark: {mark}")
        stdscr.refresh()
    else:
        stdscr.addstr("Invalid student ID. Please try again.")
        stdscr.refresh()

def calculate_gpa(student, courses):
    total_credits = 0
    weighted_sum = 0
    for course_id, mark in student['Courses'].items():
        if course_id in courses:
            credit = courses[course_id]['Credit']  # Assuming each course has a credit attribute
            total_credits += credit
            weighted_sum += mark * credit
    if total_credits == 0:
        return 0
    else:
        return weighted_sum / total_credits

def sort_students_by_gpa(students, courses):
    return sorted(students.values(), key=lambda x: calculate_gpa(x, courses), reverse=True)

def main(stdscr):
    students = {}
    courses = {}

    num_students = student_number(stdscr)
    for _ in range(num_students):
        student_info_data = student_info(stdscr)
        students[student_info_data['ID']] = student_info_data

    num_courses = course_number(stdscr)
    for _ in range(num_courses):
        course_info_data = course_info(stdscr)
        courses[course_info_data['ID']] = course_info_data
        # Adding a credit attribute to each course
        stdscr.addstr(f"Enter credit for course {course_info_data['ID']}: ")
        stdscr.refresh()
        courses[course_info_data['ID']]['Credit'] = int(stdscr.getstr().decode())

    while True:
        std
import math
import numpy as np
import curses

def student_number():
    return int(input("Input number of students in a class "))

def student_info():
    student_id = input("Enter ID: ")
    name = input("Name: ")
    dob = input("Date of birth: ")
    return {'ID': student_id,
            'Name': name,
            'DOB': dob,
            'Courses': {}}

def course_number():
    return int(input("Please choose how many courses you want to add: "))

def course_info():
    course_id = input("ID: ")
    name = input("Name: ")
    return {'ID': course_id,
            'Name': name}

def input_student_marks(students, courses):
    list_students(students)
    student_id = input("Enter the student ID for marks: ")

    if student_id in students:
        list_courses(courses)
        course_id = input("Select a course ID: ")

        if course_id in courses:
            mark = float(input("Enter mark for the selected course: "))
            # Round-down the mark to 1-digit decimal using floor function
            mark = math.floor(mark * 10) / 10
            students[student_id]['Courses'][course_id] = mark
            print(f"Mark {mark} recorded for Student ID {student_id} in Course ID {course_id}.")
        else:
            print("Invalid course ID. Please try again.")
    else:
        print("Invalid student ID. Please try again.")

def list_students(students):
    print("\nList of Students:")
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}, Name: {student_info['Name']}, DOB: {student_info['DOB']}")

def list_courses(courses):
    print("\nList of Courses:")
    for course_id, course_info in courses.items():
        print(f"Course ID: {course_id}, Name: {course_info['Name']}")

def show_student_marks(students):
    list_students(students)
    student_id = input("Enter the student ID to show marks: ")

    if student_id in students:
        print(f"\nMarks for Student ID {student_id}:")
        for course_id, mark in students[student_id]['Courses'].items():
            print(f"Course ID: {course_id}, Mark: {mark}")
    else:
        print("Invalid student ID. Please try again.")

def calculate_gpa(student, courses):
    total_credits = 0
    weighted_sum = 0
    for course_id, mark in student['Courses'].items():
        if course_id in courses:
            credit = courses[course_id]['Credit']  # Assuming each course has a credit attribute
            total_credits += credit
            weighted_sum += mark * credit
    if total_credits == 0:
        return 0
    else:
        return weighted_sum / total_credits

def sort_students_by_gpa(students, courses):
    return sorted(students.values(), key=lambda x: calculate_gpa(x, courses), reverse=True)

def main(stdscr):
    students = {}
    courses = {}

    num_students = student_number()
    for _ in range(num_students):
        student_info_data = student_info()
        students[student_info_data['ID']] = student_info_data

    num_courses = course_number()
    for _ in range(num_courses):
        course_info_data = course_info()
        courses[course_info_data['ID']] = course_info_data
        # Adding a credit attribute to each course
        courses[course_info_data['ID']]['Credit'] = int(input(f"Enter credit for course {course_info_data['ID']}: "))

    while True:
        stdscr.clear()
        stdscr.addstr("Options:\n")
        stdscr.addstr("1. Input student marks for a course\n")
        stdscr.addstr("2. List courses\n")
        stdscr.addstr("3. List students\n")
        stdscr.addstr("4. Show student marks for a given course\n")
        stdscr.addstr("5. Calculate and display GPA for a student\n")
        stdscr.addstr("6. Sort students by GPA descending\n")
        stdscr.addstr("7. Exit\n")

        choice = stdscr.getch()

        if choice == ord('1'):
            input_student_marks(students, courses)
        elif choice == ord('2'):
            list_courses(courses)
        elif choice == ord('3'):
            list_students(students)
        elif choice == ord('4'):
            show_student_marks(students)
        elif choice == ord('5'):
            list_students(students)
            student_id = input("Enter the student ID to calculate GPA: ")
            if student_id in students:
                gpa = calculate_gpa(students[student_id], courses)
                print(f"GPA for Student ID {student_id}: {gpa:.2f}")
            else:
                print("Invalid student ID. Please try again.")
        elif choice == ord('6'):
            sorted_students = sort_students_by_gpa(students, courses)
            print("\nStudents sorted by GPA (descending):")
            for student in sorted_students:
                print(f"Student ID: {student['ID']}, Name: {student['Name']}, GPA: {calculate_gpa(student, courses):.2f}")
        elif choice == ord('7'):
            print("Exiting the program.")
            break
        else:
            stdscr.addstr("You know this is not your right.\n")

curses.wrapper(main)

