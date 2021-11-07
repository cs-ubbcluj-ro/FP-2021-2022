"""
    seminar 4 rectangle -> [[0,0], [4,3]] (list of (x1,y1), (x2,y2) positions)

    what are the problems here?
        - no one tells you this is a rectangle (type(X) == list)
        - rect[1][0] = 0 -> turns the rect into a line and you can't stop it :)
        - a lot of nice-to-haves from Python are missing

    many of these you can solve using classes (create your own data type)
    data type = domain + operations
"""


class rectangle:
    """
    Class rectagle (class = blueprint)
    """

    # C# / Java
    # private int x1;

    # C++
    # private: int x1;

    def __init__(self, x1, y1, x2, y2):
        """
        constructor for rectangle data type
        constructor = special function to turn a class into an object
        """
        if x1 >= x2 or y1 >= y2:
            raise ValueError("x2 must be > x1, y2 must be > y1!")

        '''
        Python convention for accessing fields (variables) or methods
            name start in lowercase => public
            name start in _ or __ => private
            
            _ => convention not to use, but it still works
            __ => Python name mangling (Python renames it)
        '''
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    '''
    Getter and and setter version
    
    def set_y2(self, y2):
        if y2 < 0 or y2 > 20 or self.__y1 >= y2:
            raise ValueError("Invalid value for Y2!")
        self.__y2 = y2

    def get_y2(self):
        return self.__y2
    '''

    '''
    Properties version
    '''

    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, y2):
        if y2 < 0 or y2 > 20 or self.__y1 >= y2:
            raise ValueError("Invalid value for Y2!")
        self.__y2 = y2

# def rectangle():
#     pass


# rect is an object (we used the class blueprint to create an instance)
# objects take up memory space, show up in the program
# classes don't
# rect = rectangle()

# how do i customize the rectangle ??

rect = rectangle(0, 0, 4, 3)
another_rect = rectangle(1, 1, 9, 8)

rect.y2 += 10
rect.y2 += 10
print(rect.y2)

# ??

# rect.__y2 += 100

# this code is a bit too complicated
# rect.set_y2(rect.get_y2() + 10)
# rect.y2 = rect.y2 + 100
#
# print(rect.get_y2())

# print(another_rect.y2)

print(rect)
print(type(rect))
print(type(list()))
print(type("rect"))
