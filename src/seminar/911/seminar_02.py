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
    return student_id, student_name, student_grade


# use getters / setters to access / modify student fields
def get_id(student):
    return student[STUDENT_ID]


def get_name(student):
    return student[STUDENT_NAME]


def get_grade(student):
    return student[STUDENT_GRADE]


# Non-student specific code
def generate_students():
    return [create_student('116', "Bodnar Andreea", 8), create_student('117', "Pop Marius", 9),
            create_student('118', "Lazar Lucian", 10), create_student('119', "Astalus Marcel", 6)]


"""
    UI functions go here
"""


def add_student_ui():
    pass


def show_all_students(student_list):
    # First we calculate the longest student name
    just_limit = -1
    for student in student_list:
        just_limit = max(just_limit, len(get_name(student)))

    for student in student_list:
        # Student names are justified by the longest one
        print(get_id(student), get_name(student).rjust(just_limit + 1), str(get_grade(student)).rjust(2))


def print_menu():
    print("1. Add student")
    print("3. Show all students")
    print("5. Exit")


def start():
    student_list = generate_students()

    while True:
        print_menu()
        option = input("Enter option =")

        if option == '1':
            add_student_ui()
        elif option == '3':
            show_all_students(student_list)
        elif option == '5':
            return
        else:
            print("Invalid option!")


start()
