"""
Functionalities will be available using a menu or commands:
1. Generate 'n' rectangles
    random.randint(a,b) -> use to generate random integers
    - n is a positive integer read from the keyboard.
    - program generates and stores n distinct rectangles (distinct = at least one different corner),
    - each rectangle is completely enclosed in the square defined by corners (0,0) and (20,20)
2. Display all rectangle data, sorted descending by area
    rectangle: (0,0) - (10,10) -> area is 100 (0,0), (0,10), (10,0), (10,10)
    rectangle: (14,15) - (18,18) -> area is 12
    - display area and coordinates for each rectangle, using right justification (str.rjust)
3. Delete all rectangles that have at least one corner below the line x = y

"""
from functions import *
from rectangle import *


class ui:
    def __init__(self):
        self._func = functions()

    def generate_n_rectangles(self):
        n = int(input("n = "))
        while n:
            r = generate_a_rectangle()
            if self._func.check_previous_rectangles_for_uniqueness(r):
                # TODO Add add_rectangle to functions
                # rectangle_list.append(r)
                n -= 1
        print("Rectangles generated successfully")

    def display_rectangles(self):
        list_of_sorted_rectangles = self._func.rectangles_list_by_area()
        for i in range(0, len(list_of_sorted_rectangles)):
            string = "Rectangle " + str(i) + ": " + string_for_rectangle(list_of_sorted_rectangles[i])
            print(string)

    def delete_rectangles_below_line_UI(self):
        self._func.delete_rectangles_below_the_line()
        print("Rectangles deleted successfully")

    def show_menu(self):
        print("1. Generate n rectangles")
        print("2. Display all rectangles, sorted descending by area")
        print("3. Delete all rectangles that have at least one corner below the line x = y")
        print("4. Exit")

    def start(self):
        # rectangle_list = []

        while True:
            self.show_menu()
            x = input("Choose option: ")
            if x == '4':
                return
            elif x == '1':
                self._func.generate_n_rectangles()
            elif x == '2':
                self._func.display_rectangles()
            elif x == '3':
                self._func.delete_rectangles_below_line_UI()
            else:
                print("Option does not exist")


console = ui()
console.start()
