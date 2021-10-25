import rectangle
# from rectangle import rectangle
from random import randint


class functions:
    def __init__(self):
        self._rectangles = []

    def generate_rectangles(self, n):
        for i in range(n):
            x1 = randint(0, 15)
            x2 = randint(x1 + 1, 20)

            y1 = randint(0, 15)
            y2 = randint(y1 + 1, 20)

            self._rectangles.append(rectangle.rectangle(x1, y1, x2, y2))

    def sort_rectangles(self):
        return sorted(self._rectangles, reverse=True, key=max_side)


def max_side(rect):
    return max(rect.width, rect.height)
