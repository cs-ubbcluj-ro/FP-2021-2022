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

"""
    Non-UI functions go here
"""


def init_circles():
    """
    Create a few test circles
    :return: List of created circles
    """
    return [create_circle(0, 0, 1), create_circle(1, 1, 2), create_circle(2, 1, 3), create_circle(3, 3, 3)]


# Circle functions are here
# circle = [1, 2, 3] -> center at (1,2) and radius 3

# Decouple using the circle from the way it's represented


def create_circle(x, y, rad):
    """
    Function to create a circle object
    :param x,y - circle center
    :param rad - circle radius, rad > 0
    :return The new circle, or None if circle could not be created
    """
    if rad < 0:
        return None  # we learn about exceptions next week !?
    return [x, y, rad]


# We use 'setters' and 'getters'

def get_center(circle):
    return circle[0], circle[1]  # returns a tuple, so no worries


def get_radius(circle):
    return circle[2]


def equal_circles(circle_1, circle_2):
    # TODO Shallow or deep checking !?
    return get_center(circle_1) == get_center(circle_2)


def add_circle(circle_list, circle):
    """
    Add a new circle to the list
    :param circle_list: The list of circles
    :param circle: The new circle
    :return: True if circle was added successfully, False otherwise
    """
    for circ in circle_list:
        if equal_circles(circ, circle):
            return False
    circle_list.append(circle)
    return True


"""
    UI goes here
"""


def delete_circle_ui(circle_list):
    show_all_circles(circle_list)
    # TODO Crash if read value not actual int
    index = int(input("Which circle would you like to delete? "))

    if index < 1 or index > len(circle_list):
        print("Invalid index")
    else:
        circle_list.pop(index - 1)


def add_circle_ui(circle_list):
    # TODO Crash if read values not actual ints
    circle_x = int(input("Enter x="))
    circle_y = int(input("Enter y="))
    circle_rad = int(input("Enter radius="))

    circle = create_circle(circle_x, circle_y, circle_rad)
    if circle is None:
        # Radius might be < 0
        print('Invalid circle')
    elif add_circle(circle_list, circle) == False:
        print("Two circles cannot have the same center")
    else:
        print("Circle added successfully!")


def show_all_circles(circles):
    count = 1
    for circle in circles:
        print(str(count) + '/ center at ' + str(get_center(circle)) + " radius = " + str(get_radius(circle)))
        count += 1


def print_menu():
    print("1. Add circle")
    print("2. Delete circle")
    print("3. Show all circles")
    print("5. Exit")


def start():
    circle_list = init_circles()

    while True:
        print_menu()
        option = input("User option: ")

        if option == '1':
            add_circle_ui(circle_list)
        elif option == '2':
            delete_circle_ui(circle_list)
        elif option == '3':
            show_all_circles(circle_list)
        elif option == '5':
            return
        else:
            print("Option does not exist")


start()
