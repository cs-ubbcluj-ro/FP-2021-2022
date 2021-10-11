"""
Seminar 3
    -> add Exceptions
    -> implement command-based user interface
        add 100, Pop Marian, 5                           # add student
        add 100, Pop Marian, 5; 101, Damian Liliana, 10  # add student(s)
        delete 2,3, 4, 6                                 # delete students having one of those id's
        delete 2 - 10                                    # delete all students where 2 <= id <= 10
        list                                             # display the list of students
        exit
    -> add unit tests
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
    :except ValueError in case student could not be created
    """
    if len(student_id) < 1 or len(student_name) < 3 or student_grade < 1 or student_grade > 10:
        raise ValueError('Cannot create student using given data!')
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
    :except ValueError in case duplicate student id
    """
    for s in student_list:
        if get_id(student) == get_id(s):
            raise ValueError("Duplicate student id!")
    student_list.append(student)


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


def add_students_command(student_list, command_params):
    """
    add 100, Pop Marian, 5                           # add student
    add 100, Pop Marian, 5; 101, Damian Liliana, 10  # add student(s)
    """
    student_tokens = command_params.split(";")
    for tokens in student_tokens:
        try:
            student_id, student_name, student_grade = tokens.split(',')
            student = create_student(student_id.strip(), student_name.strip(), int(student_grade.strip()))
            add_student(student_list, student)
        except ValueError as ve:
            print(str(ve))


def delete_student_ui(student_list):
    student_id = input("Student id ")
    if not delete_student(student_list, student_id):
        print("Student could not be deleted")


def add_student_ui(student_list):
    student_id = input("Student id ")
    student_name = input("Student name ")

    '''
    RN Here we have 2 ways of handling errors -> C-way (return codes), and Python way (exceptions)
    Return codes:
        -> 0 on success (usually)
        -> 1 in case of error_1, 2 if error_2 etc.
        -> it's implicit, not explicit => only works if you check return values
        
    Exceptions:
        -> explicit (Python mantra says explicit >> implicit)
        -> You can see the error-handling code at work
    '''

    try:
        student_grade = int(input("Student grade "))
        student = create_student(student_id, student_name, student_grade)
        add_student(student_list, student)
    except ValueError as ve:
        print(str(ve))


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


def start_menu():
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


def start_command():
    """
    add 100, Pop Marian, 5                           # add student
    add 100, Pop Marian, 5; 101, Damian Liliana, 10  # add student(s)
    delete 2,3, 4, 6                                 # delete students having one of those id's
    delete 2 - 10                                    # delete all students where 2 <= id <= 10
    list                                             # display the list of students
    exit
    """
    student_list = generate_students()

    while True:
        command = input("prompt> ")
        tokens = command.split(" ", maxsplit=1)
        command_word = tokens[0]
        command_params = tokens[1] if len(tokens) == 2 else None
        print(command_word, command_params)

        if command_word == 'add':
            add_students_command(student_list, command_params)
        elif command_word == 'list':
            show_all_students(student_list)
        elif command_word == 'exit':
            return
        else:
            print("Bad command!")

    # start_menu()


start_command()
