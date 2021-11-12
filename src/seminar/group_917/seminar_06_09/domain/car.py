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
    :param n:
    :return: List of n cars generated pseudo-randomly
    """
    result = []
    for i in range(n):
        # TODO Generate car here
        """
        Car('100', 'CJ 10 WER', 'Dacia', 'Sandero', 'red')
        
        we need list of manufacturers, models and colors 
        
        1. Generate the ID 
            option 1 - list of random numbers to pop() from
            option 2 - start from a number and increment by 1
        2. Generate license plate number
            - We need a list of existing counties (an example, not exhaustive)
            - County is not 'B'
                - Generate a random number in [1,99], and if <10 append '0' at the beggining ('05')
            - County is 'B'
                - Generate a random number in [1,999], and if <10 append '0' at the beggining ('05')
            - Combination of three letters -> random.choices(string.ascii_uppercase, k=3)
            !! Check that license plate is unique!
        3. Have a dictionary where keys are car manufacturers (e.g. Audi, Skoda, Dacia) and values are lists of models
        for each manufacturer (e.g. [A4, Q3], [Fabia, Octavia], [Lodgy, Dokker], respectively)
        4. List of hard-coded colors (['red','blue','yellow','green'])
        """
        # result.append(car)
        pass

    return result
