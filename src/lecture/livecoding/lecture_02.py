"""
Create a calculator program for rational numbers with the following functionalities:
    + add a rational number to the calculator
    u undo the last operation (store the previous result!? use a stack!?)
    x exit
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
        return None

    d = math.gcd(numerator, denominator)
    return [numerator // d, denominator // d]  # // integer division


def get_numerator(q):
    return q[0]


def get_denominator(q):
    return q[1]


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
def init_calculator():
    pass


"""
    UI functions
        - "talk" to the program's user
        - rely on the non-UI functions to solve the requirements
"""


def print_menu():
    print("\t+ add number to calculator")
    print("\tu undo the last operation")
    print("\tx exit")


def start():
    print_menu()

    while True:
        # initialize calculator -> 0 default value
        option = input("Option: ")
        # perform operation
        if option == 'x':
            return
        else:
            print("Invalid input")

# start()
