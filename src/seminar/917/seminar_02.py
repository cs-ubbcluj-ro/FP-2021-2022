"""
Write an application that manages a list of circles.
Each circle has a unique center (x,y - ints) and a positive radius (int).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a circle
        - adds the given circle to the list.
        - error if circle with given center already exists, the center or radius not given, empty or radius < 0

    2. Delete a circle
        - deletes the circle with the given center
        - error if non-existing center is given

    3. Show all circles
        - shows all circles
        (bonus: sort in descending order of radius)

    4. Show circles that intersect a given one
        - select a circle from the list of existing circles
        - print those which intersect it
        (bonus: sort printed circles by descending order of radius)

    5. exit
        - exit the program

    Observations:
        - When starting the program, it already has data entered!
        - We have two types of functions: those for the UI and those for functionalities
        - We have specification for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It can report errors from non-UI functions too!
        - You can crash the program by providing incorrect input
        - Make sure you understand the circle's representation
        - We reuse functions across functionalities. Less code to write and test!
        - We can develop this program in a feature-driven manner by going through functionalities
        - We don't use global variables!
"""