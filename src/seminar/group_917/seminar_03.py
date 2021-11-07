"""
Seminar 3
    -> add Exceptions
    -> implement command-based user interface
        add 0,0,1
        delete 0,0; 1,1 # delete circles at center (0,0) and (1,1)
        list # display the list of circles
        exit

    -> add unit tests
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
    :except ValueError if rad <= 0
    """
    if rad <= 0:
        raise ValueError('Circle radius must be >0')
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
    :except: Circle with given center already exists
    """
    for circ in circle_list:
        if equal_circles(circ, circle):
            """
            Raising an exception allows us to tell the user what went wrong without using print
            (we're in non-UI section of code)
            """
            raise ValueError('Duplicate circles')
    circle_list.append(circle)


def split_command(command):
    """
    Divide user command into command word and parameters
    :param command: User command
    :return: [command word, command parameters]
    """
    # Remove whitespace at beginning & end of command
    command = command.strip()
    # Remove whitespace between command word and params
    aux = command.split(sep=' ', maxsplit=1)
    return [aux[0].strip().lower(), aux[1].strip()] if len(aux) == 2 else [aux[0].strip().lower(), None]


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


def add_circle_command_ui(circle_list, command_params):
    # add 0, 0, 1

    aux = []
    params = command_params.split(',')
    for param in params:
        aux.append(param.strip())

    circle_x = int(aux[0])
    circle_y = int(aux[1])
    circle_rad = int(aux[2])
    add_circle(circle_list, create_circle(circle_x, circle_y, circle_rad))


def add_circle_ui(circle_list):
    # ValueError is a Python exception, happens when a value is not what it should be
    '''
    2 major ways of handling errors:
        C-way - return an error code
            - only works if someone checks the error code
        Exception-based
            + it forces you to handle possible issues
            + explicit -> you can see the error being handled
    '''
    try:
        circle_x = int(input("Enter x="))
        circle_y = int(input("Enter y="))
        circle_rad = int(input("Enter radius="))

        circle = create_circle(circle_x, circle_y, circle_rad)
        add_circle(circle_list, circle)
    except ValueError as ve:
        print(str(ve))
        return


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


def start_menu():
    """
    Start menu-based UI
    """
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


def start_command():
    """
    Start command-based UI

    <command word> <command parameters>

    add 0,0,1 # (add circle at (0,0) radius 1)
    delete 0,0; 1,1 # delete circles at center (0,0) and (1,1)
    list # display the list of circles
    exit
    """
    circle_list = init_circles()

    while True:
        command = input("prompt> ")
        command_word, command_params = split_command(command)

        try:
            if command_word == 'list':
                # Try to reuse as many functions as possible
                show_all_circles(circle_list)
            elif command_word == 'add':
                # Might quit with ValueError
                add_circle_command_ui(circle_list, command_params)
            elif command_word == 'exit':
                return
            else:
                print("Command does not exist")
        except ValueError as ve:
            print(str(ve))


start_command()
# start_menu()
