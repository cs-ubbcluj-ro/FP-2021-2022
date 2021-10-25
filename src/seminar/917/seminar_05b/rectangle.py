"""
Write a program that manages rectangles. Each rectangle is defined by two of its opposing corners, having coordinates
(x1,y1) and (x2,y2) (for example, points (0,0) and (1,1) define a 'unit rectangle').
"""


class point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class rectangle:
    def __init__(self, p1, p2):
        # TODO p1.x < p2.x and p1.y<p2.y
        self._p1 = p1
        self._p2 = p2

    def equal(self, rect):
        """
        Is this rectangle equal to rectangle rect?
        :param rect:
        :return:
        """
        if not isinstance(rect, rectangle):
            raise TypeError("Parameter not a rectangle")
        return self._p1 == rect._p1 and self._p2 == rect._p2

    def area(self):
        return abs((self._p2.x - self._p1.x) * (self._p2.y - self._p1.y))

    def __str__(self):
        return "Rectangle " + str(self._p1) + " -> " + str(self._p2)


rect = rectangle(point(1, 1), point(4, 3))
print(rect)
print(rect.area())


def create_point(x, y):
    return {"x": x, "y": y}


def get_x_from_point(point):
    return point["x"]


def get_y_from_point(point):
    return point["y"]


def points_on_different_lines(p1, p2):
    if get_x_from_point(p1) == get_x_from_point(p2) or get_y_from_point(p1) == get_y_from_point(p2):
        return False
    return True


def equal_points(p1, p2):
    if get_x_from_point(p1) == get_x_from_point(p2) and get_y_from_point(p1) == get_y_from_point(p2):
        return True
    return False


def string_for_point(point):
    string = "(" + str(get_x_from_point(point)) + "," + str(get_y_from_point(point)) + ")"
    return string


def below_the_line(point):
    if get_x_from_point(point) < get_y_from_point(point):
        return True
    return False


def create_rectangle(p1, p2):
    return {"corner 1": p1, "corner 2": p2}


def get_corner1(rectangle):
    return rectangle["corner 1"]


def get_corner2(rectangle):
    return rectangle["corner 2"]


def equal_rectangles(r1, r2):
    if equal_points(get_corner1(r1), get_corner1(r2)) == True and equal_points(get_corner2(r1),
                                                                               get_corner2(r2)) == True or equal_points(
        get_corner1(r1), get_corner2(r2)) == True and equal_points(get_corner2(r1), get_corner1(r2)) == True:
        return True
    return False


def area_of_rectangle(r):
    """
    rectangle: (0,0) - (10,10) -> area is 100 (0,0), (0,10), (10,0), (10,10)
    rectangle: (14,15) - (18,18) -> area is 12
    :param r:
    :return:
    """
    l1 = get_x_from_point(get_corner1(r)) - get_x_from_point(get_corner2(r))
    l1 = abs(l1)
    l2 = get_y_from_point(get_corner1(r)) - get_y_from_point(get_corner2(r))
    l2 = abs(l2)
    return l1 * l2


def string_for_rectangle(r):
    string = string_for_point(get_corner1(r)) + " - " + string_for_point(get_corner2(r)) + " area = " + str(
        area_of_rectangle(r))
    return string
