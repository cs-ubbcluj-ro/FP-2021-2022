"""
Implement the domain class
"""


class Car:
    def __init__(self, id_, license_plate="n/a", make='', model='', color=''):
        self._id = id_
        self._license_plate = license_plate
        self._make = make
        self._model = model
        self._color = color

    @property
    def id(self):
        return self._id

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self, new_license_plate):
        self._license_plate = new_license_plate

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    def __eq__(self, z):
        if isinstance(z, Car) is False:
            return False
        return self.id == z.id

    def __str__(self):
        return "Id: " + str(
            self.id) + ", License: " + self.license_plate + ", Car type: " + self.make + ", " + self.model

    def __repr__(self):
        return str(self)
