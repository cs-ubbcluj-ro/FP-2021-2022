"""
Type = Domain + Operations
Predefined types -> int, str, list, dict, tuple, function, class
User-defined types <=> defining our own classes

How to represent a rectangle???
    Two of its opposing corners, having coordinates (x1,y1) and (x2,y2)

    V1 (week 4)
            rect = ((1,1),(4,3))
            list of rectangles wondering around in the program :)
        problem?
            -> tuples are immutable (use a list, dict)?
            -> Python does not recognize ((1,1),(4,3)) as a rectangle
            -> rect[0][1] = "abcd" -> easier to break the program
            -> list of rectangles could be changed by any function
    V2 (week 5+)
        we use classes
"""


class rectangle:
    """
    C++ (hopefully)

    public: int x1,x2,y1,y2;

    protected/private -> Python doesn't have an <=>

    Access modifiers the Python way:
        _  -> don't access from outside the class (convention)
        __ ->  don't access from outside the class (Python name mangling)
        other_name -> they are assumed public
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Constructor for rectangle
        x1 < x2, y1 < y2
        """
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Bad rectangle")

        self.__rect_x1 = x1  # this.x1 = x1; <-- C++
        self.__rect_x2 = x2
        self.__rect_y1 = y1
        self.__rect_y2 = y2

    @property
    def x1(self):
        return self.__rect_x1

    @x1.setter
    def x1(self, new_value):
        if self.__rect_x2 <= new_value:
            raise ValueError("Bad rectangle!")
        self.__rect_x1 = new_value

    @property
    def x2(self):
        return self.__rect_x2

    @property
    def y1(self):
        return self.__rect_y1

    @property
    def y2(self):
        return self.__rect_y2

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    def __str__(self):
        return "rectangle (" + str(self.x1) + "," + str(self.y1) + ")-(" + str(self.x2) + "," + str(self.y2) + ")"

# r = rectangle(1, 1, 4, 3)
# r1 = rectangle(1, 1, 4, 3)
# # r.rect_x1 = "ABCD"
#
#
# print(r.x1)
# r.x1 *= 2
# print(r.x1)
#
# # print(r.rect_x1)
# # print(type(r))
