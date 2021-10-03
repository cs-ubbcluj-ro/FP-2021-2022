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