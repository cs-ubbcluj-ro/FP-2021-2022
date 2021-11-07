""""
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
import random
from rectangle import *


class functions:
    def __init__(self):
        self._rectangle_list = []

    def check_previous_rectangles_for_uniqueness(self, r):
        for rect in self._rectangle_list:
            if equal_rectangles(rect, r):
                return False
        return True

    def delete_rectangles_below_the_line(self):
        i = 0
        while i < len(self._rectangle_list):
            if below_the_line(get_corner1(self._rectangle_list[i])) == True or below_the_line(
                    get_corner2(self._rectangle_list[i])) == True:
                self._rectangle_list.pop(i)
                i -= 1
            i += 1

    def rectangles_list_by_area(self):
        rectangles_sorted = sorted(self._rectangle_list, key=area_of_rectangle, reverse=True)
        return rectangles_sorted


def generate_a_rectangle():
    p1 = create_point(0, 0)
    p2 = create_point(0, 0)
    while equal_points(p1, p2) and points_on_different_lines(p1, p2) == False:
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        p1 = create_point(x, y)
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        p2 = create_point(a, b)
    return create_rectangle(p1, p2)
