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
            1. two circles are tangent !?
            2. two circles have a common area !?
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
import math

"""
    Non-UI functions 
        - no print, no input statements
"""


# Circle functions go here
# dict: {'x' : 1,'y' : 2, 'rad' : 3} is circle with center at (1,2) and radius 3
# list: [1,2,3] is circle with center at (1,2) and radius 3 (represented using a list)
# We want to hide the circle's representation from the outside world (hide complexity)


def create_circle(x, y, radius):
    """
    Create a new circle
    :param x: The X coord of the circle center
    :param y: The Y coord of the circle center
    :param radius: Circle radius, must be a positive integer
    :return: A newly created circle, None if circle could not be created
    """
    # if type(x) != int:
    #     return None
    if radius < 1:
        return None  # NoneType, means the absence of a value
    return [x, y, radius]
    # return {'x': x, 'y': y, 'rad': radius}


# Write getters/setters for circle center and radius
def get_center(circle):
    return circle[0], circle[1]
    # return circle['x'], circle['y']


def get_radius(circle):
    return circle[2]
    # return circle['rad']


def build_tangent_circles(circle_list, circle):
    """
    Return a list of the circles tangent with the given one
    :param circle_list: The list of all circles
    :param circle: Our circle :)
    :return: A list of all circles that are tangent with the given one
    """
    result = []
    for circ in circle_list:
        if circles_are_tangent(circ, circle):
            result.append(circ)
    return result


def circles_are_tangent(circle_1, circle_2):
    """
    Determines whether the two circles are tangent
    :param circle_1: First
    :param circle_2: Second circle
    :return: True if they are tangent, False otherwise
    """
    c1 = get_center(circle_1)
    c2 = get_center(circle_2)

    r1 = get_radius(circle_1)
    r2 = get_radius(circle_2)

    center_distance = math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
    return center_distance == r1 + r2


# Test function is named test_<function that is tested>
def test_circles_are_tangent():
    # assert crashes if the expression is False
    assert circles_are_tangent(create_circle(0, 0, 1), create_circle(2, 0, 1)) == True
    assert circles_are_tangent(create_circle(0, 0, 1), create_circle(1, 0, 1)) == False
    # One circle contained in the other, we don't consider them tangent for simplicity
    assert circles_are_tangent(create_circle(0, 0, 5), create_circle(4, 0, 1)) == False


# test_circles_are_tangent()

# Non-circle functions
def add_circle(circle_list, circle):
    """
    Adds a new circle to the list
    :param circle_list: The list of circles
    :param circle: The new circle
    :return: True on success, False if circle could not be added
    """
    for c in circle_list:
        if get_center(c) == get_center(circle):
            return False
    circle_list.append(circle)
    return True


def init_circles():
    """
    Create a few circles to have at program startup
    :return: A list of circles
    """
    return [create_circle(1, 1, 1), create_circle(1, 2, 3), create_circle(2, 1, 7), create_circle(3, 3, 2)]


"""
    UI functions are here
        - program talks to the user via print/input statements 
"""


def show_circles(circle_list):
    index = 1
    for circle in circle_list:
        print(str(index) + "/ center at " + str(get_center(circle)) + " radius of " + str(get_radius(circle)))
        index += 1


def show_circles_intersect_ui(circle_list):
    show_circles(circle_list)

    # TODO Crash if entered values cannot be converted to int
    # TODO Validate index!
    index = int(input("Select circle: "))

    circle = circle_list[index - 1]
    tangent_circles = build_tangent_circles(circle_list, circle)
    show_circles(tangent_circles)

def add_circle_ui(circle_list):
    # How do we represent a circle? -> each circle is represented using a dict
    # Where do we add it? -> we keep a list of circles

    # TODO Crash if entered values cannot be converted to ints
    circle_x = int(input("Enter X ="))
    circle_y = int(input("Enter Y ="))
    circle_rad = int(input("Enter radius ="))

    circ = create_circle(circle_x, circle_y, circle_rad)
    if circ is None:
        print("Invalid circle")
        return
    if not add_circle(circle_list, circ):
        print("Circle could not be added")


def print_menu():
    print("1. Add circle")
    print("3. Show circles")
    print("4. Show circles that intersect a given one")
    print("5. Exit")


def start():
    circle_list = init_circles()

    while True:
        print_menu()
        option = input("Enter option ")

        if option == '1':
            add_circle_ui(circle_list)
        elif option == '3':
            show_circles(circle_list)
        elif option == '4':
            show_circles_intersect_ui(circle_list)
        elif option == '5':
            # Exit the closest loop
            break
        else:
            print("Invalid option")


start()
