"""
Lecture 02

    Create a calculator program for rational numbers with the following functionalities:
        + add a rational number to the calculator
        u undo the last operation (store the previous result!? use a stack!?)
        x exit

Lecture 03
    Turn this into a command-driven UI
    Implement undo functionality
    Practice test-driven development a bit :)

    Test how we can change the UI we use (menu vs. command) and change the number representation
"""
import math

"""
    Functions
        - they have a specification (what a function does)
        - each function should do one single
            => Single Responsibility Principle (good programming practice)

    Program
        - write small parts of the program and run it OFTEN
        - git commit when a new functionality works
        - work on functionalities one by one 
"""

"""
    Non-UI functions
        - there will be no print/input calls here
        - these functions will not call other functions that use print/input
        - these functions communicate via parameters & return type and value
"""


# How do we store a rational number?
# 3/7 -> [3,7], 0/1 -> [0,1]
def create_rational(numerator=0, denominator=1):
    """
    Create a new rational number
    :param numerator: Number numerator (default 0)
    :param denominator: Number denominator (default 1), cannot be 0
    :return: New rational number (simplified), or None if could not be created
    """
    if denominator == 0:
        # Failing silently
        # return None
        # Fail loudly
        raise ValueError('Cannot create with denom = 0')

    d = math.gcd(numerator, denominator)
    return [numerator // d, denominator // d]  # // integer division
    # return {'n': numerator // d, 'd': denominator // d}


def get_numerator(q):
    return q[0]
    # return q['n']


def get_denominator(q):
    return q[1]
    # return q['d']


def to_str(q):
    return str(get_numerator(q)) + "/" + str(get_denominator(q))


def add(q1, q2):
    """
    Sum of rational numbers
    """
    new_num = get_numerator(q1) * get_denominator(q2) + get_numerator(q2) * get_denominator(q1)
    new_denom = get_denominator(q1) * get_denominator(q2)
    # calling create_rational automatically simplifies the new fraction
    return create_rational(new_num, new_denom)


def test_to_str():
    assert to_str(create_rational()) == '0/1'
    assert to_str(create_rational(3, 6)) == '1/2'
    assert to_str(create_rational(300, 600)) == '1/2'
    assert to_str(create_rational(3)) == '3/1'


def test_add():
    """
    Test function for add function
    Test functions:
        - Named test_<name of tested function>
        - Don't take parameters (simple to run)
        - Don't return anything
        - You can run them in any order
        - Crash (assert) if tested function does not behave properly
    """
    # TODO Implement equal(q1,q2)
    # assert <condition>, fails if <condition> is False
    assert create_rational() == add(create_rational(), create_rational())  # ?
    assert create_rational(1) == add(create_rational(1), create_rational())  # ?
    assert create_rational(2, 3) == add(create_rational(1, 3), create_rational(1, 3))  # ?
    assert create_rational(1) == add(create_rational(1, 3), create_rational(2, 3))  # ?
    assert create_rational(1) == add(create_rational(1, 2), create_rational(500, 1000))  # ?
    assert create_rational(21, 47) == add(create_rational(13, 47), create_rational(8, 47))  # ?


test_add()
test_to_str()


# q = create_rational(100, 50)
# print(q)  # 2/1
# print(to_str(q))  # 2/1


# How do we store the calculator's state?
# Keep list of intermediate results for undo operation
# Current calculator value is the last item in the list
def init_calculator():
    return [create_rational()]  # calc with default value 0/1 and no history for undo


def get_value_calculator(calc):
    return calc[-1]  # last item in calculator


def set_value_calculator(calc, q):
    calc.append(q)


def add_calculator(calc, q):
    """
    Add a number to the calculator
    :param calc: Calculator instance
    :param q: Number
    :return: ?
    """
    new_total = add(q, get_value_calculator(calc))
    set_value_calculator(calc, new_total)


def undo_calculator(calc):
    """
    Undo the last operation carried out
    :param calc:  Calculator instance
    :return: ?
    """
    if len(calc) == 1:
        raise ValueError("Cannot undo operation")
    calc.pop()


#
# Non-UI helper functions
#
def split_command_params(user_cmd):
    """
    Split the user's command into the command word and a parameters string
    ex:
         add 1/2, 3/4, 10/20, 0/1 -> ('add', '1/2, 3/4, 10/20, 0/1')
         undo 5                   -> ('undo', '5')
         exit                     -> ('exit', None)
    :param user_cmd: Command input by the user
    :return: A tuple of (<command word>, <command params>) in lowercase
    """
    user_cmd = user_cmd.strip()
    tokens = user_cmd.split(maxsplit=1)
    cmd_word = tokens[0].lower() if len(tokens) > 0 else None  # ?:
    cmd_param = tokens[1].lower() if len(tokens) == 2 else None  # ?:

    return cmd_word, cmd_param


"""
    Test Driven Development 101 (07:50 crash course)
        We use it at function level (to test each function individually)
        
        1. Write the function signature & specification 
        2. Write a test function with test cases (use assert - for now, unittest later)
        3. Run the test function and see it fail
        4. Code the target function until the tests pass
        5. Optimize target function (test by re-running the test function(s))
"""


def test_split_command_params():
    # assert crashes if False, does nothing if True
    assert split_command_params('exit') == ('exit', None)
    assert split_command_params('eXiT') == ('exit', None)
    assert split_command_params('add 1/2, 3/4, 10/20, 0/1') == ('add', '1/2, 3/4, 10/20, 0/1')
    assert split_command_params('   ADD    1/2, 3/4, 10/20, 0/1   ') == ('add', '1/2, 3/4, 10/20, 0/1')
    assert split_command_params('add 1/2') == ('add', '1/2')
    # split command does not care about the actual values entered
    assert split_command_params('add 1/0') == ('add', '1/0')
    assert split_command_params('undo     5') == ('undo', '5')
    assert split_command_params('     undo') == ('undo', None)
    # This is a bad command, but still should be split
    assert split_command_params('undo abcd') == ('undo', 'abcd')


# test_split_command_params()


"""
    UI functions
        - "talk" to the program's user
        - rely on the non-UI functions to solve the requirements
"""


def undo_command_run(calc, params):
    if params is None:
        steps = 1
    else:
        try:
            steps = int(params.strip())
        except ValueError as ve:
            print(ve)
            return

    while steps > 0:
        try:
            undo_calculator(calc)
        except ValueError as ve:
            print(ve)
            return
        steps -= 1


def add_command_run(calc, params):
    """
    1/2, 3/4, 10/20   ,   0/1 # add those numbers to the calc
    :param calc:
    :param params:
    :return:
    """
    tokens = params.split(',')
    for token in tokens:
        token = token.strip()
        num, denom = token.split('/')

        try:
            q = create_rational(int(num.strip()), int(denom.strip()))
            add_calculator(calc, q)
        except ValueError as ve:
            # TODO Raise exception into the UI
            print("Cannot add non-valid number")


def read_rational():
    n = int(input("Numerator: "))
    d = int(input("Denominator: "))
    return create_rational(n, d)


def print_menu():
    print("\t+ add number to calculator")
    print("\tu undo the last operation")
    print("\tx exit")


def start_menu_ui():
    # Don't use global vars
    calc = init_calculator()

    while True:
        print_menu()
        print("TOTAL: " + to_str(get_value_calculator(calc)))

        # initialize calculator -> 0 default value
        option = input("Option: ")

        try:
            # perform operation
            if option == 'x':
                return
            elif option == '+':
                q = read_rational()
                add_calculator(calc, q)
            elif option == 'u':
                undo_calculator(calc)
            else:
                print("Invalid input")
        except ValueError as ve:
            print(str(ve))


def start_command_ui():
    """
    Command format example for calculator
         add 1/2, 3/4, 10/20, 0/1 # add those numbers to the calc
         undo 5                   # undo the last 5 numbers added
         exit
    :return:
    """
    calc = init_calculator()

    # Init a dict with an entry for each correct command
    cmd_dict = {'add': add_command_run, 'undo': undo_command_run}

    while True:
        # Print calc value & read user input
        user_cmd = input("TOTAL " + to_str(get_value_calculator(calc)) + ">")

        # Parse user command into command word & parameters
        # unpacking the function's return
        cmd_word, cmd_params = split_command_params(user_cmd)

        if cmd_word == 'exit':
            return

        # Call the correct function for the given command
        if cmd_word not in cmd_dict:
            print("Bad command")
        else:
            cmd_dict[cmd_word](calc, cmd_params)
            # cmd_dict                             -> dictionary of commands
            # cmd_dict[cmd_word]                   -> the function reference that needs to be called
            # cmd_dict[cmd_word](calc, cmd_params) -> actual function call


# start_menu_ui()
start_command_ui()
