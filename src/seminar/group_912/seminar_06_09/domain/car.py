"""
Implement the domain class
"""


class Car:
    def __init__(self, license_plate="n/a", make='', model='', color=''):
        self._license_plate = license_plate
        self._make = make
        self._model = model
        self._color = color

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

    '''
    @property is a Python decorator 
    decorator = function that wraps color() and provides additional functionality
    '''

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    # car_1 == car_2
    def __eq__(self, z):
        if isinstance(z, Car) is False:
            return False
        return self.id == z.id

    def __str__(self):
        return "Id: " + str(
            self.id) + ", License: " + self.license_plate + ", Car type: " + self.make + ", " + self.model

    def __repr__(self):
        return str(self)


def generate_cars(n=50):
    """
    Generate a number of cars
    :param n: how many cars to generate
    :return: List of generated cars
    """
    data = []
    for i in range(n):
        # TODO Generate a random car here
        """
        How to generate a random car?
        
        1. Generate the license plate
            - Have a list of counties and randomly select one of them (random.choice(...))
            - Generate a number using randrange(1, 100) and convert to str(...)
            # if number < 10:
            #    number_str = '0' + str(number)
            #  else: 
            #    number_str = str(number)
            # <=>
            #  number_str = str(number) if number > 9 else '0' + str(number)     
                        
            - Select 3 random letters from the list of uppercase letters
                list of uppercase letters - import string / string.ascii_uppercase / random.choices
        
        2. Generate car make and model dict where keys are makers (BMW, Dacia) and the values are lists of the maker's 
           models (Serie 1, X5 and Lodgy, Dokker respectively)
           
        3. Generate color - choose from a predefined list of colors
        """
        # data.append(car)
        pass
    return data


import string
import random

print(string.ascii_uppercase)

c = Car('CJ 10 TYU', 'Dacia', 'Duster', 'blue')

print(ord('A'))
print(ord('Z'))
print(chr(70))
