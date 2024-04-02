from input import student_number, student_info, course_number, course_info
from domains.student import Student

def input_student_marks(students, courses):
    list_students(students)
    student_id = input("Enter the student ID for marks: ")

    if student_id in students:
        list_courses(courses)
        course_id = input("Select a course ID: ")

        if course_id in courses:
            mark = float(input("Enter mark for the selected course: "))
            mark = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
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

def calculate_gpa(student):
    total_credits = 0
    weighted_sum = 0
    for course_id, mark in student['Courses'].items():
        credit = 3  # Assuming all courses have 3 credits, you can modify as needed
        total_credits += credit
        weighted_sum += mark * credit
    return weighted_sum / total_credits

def sort_students_by_gpa(students):
    return sorted(students.values(), key=lambda x: calculate_gpa(x), reverse=True)

def main():
    students = {}
    courses = {}

    num_students = student_number()
    for _ in range(num_students):
        student_info_data = student_info()
        student = Student(student_info_data['ID'], student_info_data['Name'], student_info_data['DOB'])
        students[student_info_data['ID']] = student

    num_courses = course_number()
    for _ in range(num_courses):
        course_info_data = course_info()
        courses[course_info_data['ID']] = course_info_data

    while True:
        print("\nOptions:")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Sort students by GPA")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            input_student_marks(students, courses)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks(students)
        elif choice == '5':
            sorted_students = sort_students_by_gpa(students)
            print("\nStudents sorted by GPA:")
            for student in sorted_students:
                print(f"Student ID: {student['ID']}, Name: {student['Name']}, GPA: {calculate_gpa(student)}")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
