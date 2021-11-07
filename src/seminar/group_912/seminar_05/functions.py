from circles import circle
from random import randint


class functions:
    def __init__(self):
        self._circle_list = []

    def generate_circles(self, n):
        """
        Generate circles
        :param n: How many circles to create
        :return: None
        """
        for i in range(n):
            self._circle_list.append(circle(randint(1, 20), randint(1, 20), randint(1, 5)))

    def delete_circles(self, x, y, width, height):
        """
        Delete all circles in rectangle (x,y) - (x + width, y + height)
        :param x:
        :param y:
        :param width:
        :param height:
        :return: The number of deleted circles
        """
        pass

    def sort_circle_list(self):
        """
        Sort list of circles descending by radius
        :return: Sorted copy of the original list
        """
        return sorted(self._circle_list, key=get_radius, reverse=True)


def get_radius(c):
    return c.r
