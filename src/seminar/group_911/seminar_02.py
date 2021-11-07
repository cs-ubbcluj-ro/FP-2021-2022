"""
Write an application that manages a list of students.
Each student has a unique id (string), a name (string) and a grade (integer).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a student
        - adds the student with the given id, name and grade to the list.
        - error if giving existing id, the name or grade fields not given or empty

    2. Delete a student
        - deletes the student with the given id from the list
        - error if non-existing id given

    3. Show all students
        - shows all students
        (bonus: sort students in descending order of name or grade)

    4. Show students whose grade is > than given one
        (bonus: sort students by descending order of grade)

    5. exit
        - exit the program

    Observations:
        - When starting the program, it already has data entered!
        - We have two types of functions: those for the UI and those for functionalities
        - We have specification for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It can report errors from non-UI functions too!
        - You can crash the program by providing incorrect input
        - Make sure you understand the representation of student
        - We reuse functions (e.g. __showStudents) for several functionalities. Less code to write and test!
        - We can develop this program in a feature-driven manner by going through functionalities
        - We don't use global variables!
"""

"""
    Non-UI functions are here
"""
STUDENT_ID = 0
STUDENT_NAME = 1
STUDENT_GRADE = 2


# How to represent a student
# tuple: ('1123', 'Pop Andrei', 9) -> 1123 is the id, 9 is the grade student[0]
# dict: {'id' : '1123', 'name' : 'Pop Andrei', 'grade': 9} # student['id']
# code for 912/917 also has representation examples (list, dict)

def create_student(student_id, student_name, student_grade):
    """
    Create a new student
    :param student_id: Id (must not be empty)
    :param student_name: Name (name is length at least 3)
    :param student_grade: Grade (int between 1 and 10)
    :return: Student, or None if student could not be created
    """
    if len(student_id) < 1 or len(student_name) < 3 or student_grade < 1 or student_grade > 10:
        return None
    # return student_id, student_name, student_grade
    return {'id': student_id, 'name': student_name, 'grade': student_grade}


# use getters / setters to access / modify student fields
def get_id(student):
    # return student[STUDENT_ID]
    return student['id']


def get_name(student):
    # return student[STUDENT_NAME]
    return student['name']


def get_grade(student):
    # return student[STUDENT_GRADE]
    return student['grade']


# Non-student specific code
def generate_students():
    return [create_student('116', "Bodnar Andreea", 8), create_student('117', "Pop Marius", 9),
            create_student('118', "Lazar Lucian", 10), create_student('119', "Astalus Marcel", 6)]


def add_student(student_list, student):
    """
    Add a student to the list of students
    :param student_list: Student list
    :param student: New student instance
    :return: True if student successfully added, False otherwise
    """
    for s in student_list:
        if get_id(student) == get_id(s):
            return False

    student_list.append(student)
    return True


def delete_student(student_list, student_id):
    """
    Delete the student with the given ID
    :param student_list: The list of all students
    :param student_id: Student_id to delete
    :return: True on success, False if student id does not exist
    """
    for s in student_list:
        if get_id(s) == student_id:
            student_list.remove(s)
            return True
    return False


"""
    UI functions go here
"""


def delete_student_ui(student_list):
    student_id = input("Student id ")
    if not delete_student(student_list, student_id):
        print("Student could not be deleted")


def add_student_ui(student_list):
    student_id = input("Student id ")
    student_name = input("Student name ")
    # TODO Crash if values cannot be converted to an integer, or in case of empty string
    student_grade = int(input("Student grade "))

    student = create_student(student_id, student_name, student_grade)
    if student is None:
        print("Cannot create student")
        return

    if not add_student(student_list, student):
        print("Duplicate student id!")


def show_all_students(student_list):
    # key is a named argument, get_name is a reference to a function
    student_list.sort(reverse=True, key=get_grade)

    # First we calculate the longest student name
    just_limit = -1
    for student in student_list:
        just_limit = max(just_limit, len(get_name(student)))

    for student in student_list:
        # Student names are justified by the longest one
        print(get_id(student), get_name(student).rjust(just_limit + 1), str(get_grade(student)).rjust(2))


def print_menu():
    print("1. Add student")
    print("2. Delete student")
    print("3. Show all students")
    print("5. Exit")


def start():
    student_list = generate_students()

    while True:
        print_menu()
        option = input("Enter option =")

        if option == '1':
            add_student_ui(student_list)
        elif option == '2':
            delete_student_ui(student_list)
        elif option == '3':
            show_all_students(student_list)
        elif option == '5':
            return
        else:
            print("Invalid option!")


start()
