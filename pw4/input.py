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
    return int(input("Please choose how many courses you want: "))

def course_info():
    course_id = input("ID: ")
    name = input("Name: ")
    return {'ID': course_id,
            'Name': name}
