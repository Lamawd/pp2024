#Input number students
def student_number():
    return int(input( "Input number of students in a class "))
#Input student infomation
def student_info():
    student_id=input("Enter ID: ")
    name=input("Name: ")
    dob=input(" Date of birth: ")
    return{'ID': student_id,
            'Name': name,
            'DOB': dob,
            'Courses': {}}
#Input number of course
def course_number():
    return int(input("Please choose how many dead body you want: "))

# Course info
def course_info():
    course_id=input("ID: ")
    name=input("name: ")
    return{ 'ID': course_id,
           'Name': name} 
def input_student_marks(students, courses):
    list_students(students)
    student_id = input("Enter the student ID for marks: ")

    if student_id in students:
        list_courses(courses)
        course_id = input("Select a course ID: ")

        if course_id in courses:
            mark = float(input("Enter mark for the selected course: "))
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

def main():
    students = {}
    courses = {}

    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_info_data = student_info()
        students[student_info_data['ID']] = student_info_data

    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_info_data = course_info()
        courses[course_info_data['ID']] = course_info_data

    while True:
        print("\nOptions:")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            input_student_marks(students, courses)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks(students)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("You know this is not your right.")

if __name__ == "__main__":
    main()

