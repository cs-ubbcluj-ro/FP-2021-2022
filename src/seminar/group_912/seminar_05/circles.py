"""
Each circle has an (x,y) center (x,y - integers) and a the radius r
(r > 0, r is an integer)

Representing a circle:
    V1 (without classes) -> {"x" : 10, "y" : 10, "radius" : 3}
    -> list of circles wonders around in the program :)
    -> you might break this list accidentally (add a non-circle to it)
    -> type is not a circle, but acutally a dict
    -> no way to enforce costraints/safeguard ( c["y"] = "abcd" -> this is bad )

Class vs. Object:
    Class:
        -> Template, blueprint of how to create objects
        -> Does not take up memory
    Objects:
        -> Class instances
        -> They take up memory during program execution
    Class ->> Objects

    constructor -> special method that turns a class into an object
"""


class circle:
    """
    Blueprint for objects of type circle (or circles).
    We describe what we can and can't do with circles
    """

    """
    C++/C#/Java
        private -> variable can only be accessed from within the class
         public -> variable can be accessed from all code
         
    Python
        first letter of field/method name
        
        _  -> var is private by convention (you can use it, but you should not)
        __ -> var is private by name mangling (Python assigns a new name to it)
    """

    def __init__(self, x, y, r):
        """
        Constructor for Circle class
        :param x:
        :param y:
        :param r:
        """
        if r <= 0:
            raise ValueError("radius must be > 0!")
        self._center_x = x
        self._center_y = y
        self._radius = r

    @property
    def x(self):
        return self._center_x

    @x.setter
    def x(self, new_value):
        self._center_x = new_value

    @property
    def y(self):
        return self._center_y

    @y.setter
    def y(self, new_value):
        self._center_y = new_value

    @property
    def r(self):
        return self._radius

    @r.setter
    def r(self, new_value):
        if new_value <= 0:
            raise ValueError("radius must be > 0!")
        self._radius = new_value

    def __str__(self):
        return "center at (" + str(self.x) + "," + str(self.y) + "), radius =" + str(self.r)

# Created an object of type circle
# c1 = circle(10, 10, 3)
# c2 = circle(99, 99, 11)

# c1.set_x(15)
# circle.set_x(c1, 15)

# c2.set_x(2 * c2.get_x())
# c2.x *= 2
# c2.r = -1

# print(c.__x)
# c.x = "abcd"
# print(c1.x)
# print(c2.x)
# print(type(c1))
