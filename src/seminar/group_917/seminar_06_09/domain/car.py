"""
Implement the domain class
"""

'''
V1 - Act as a constant field
V2 - We'll read this from a file
'''
CAR_COUNTIES = ['AB', 'CJ', 'B', 'CT', 'IS', 'TL']


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

    # ==  car_1 == car_2 ?
    def __eq__(self, z):
        if isinstance(z, Car) is False:
            return False
        return self.id == z.id

    def __str__(self):
        return "Id: " + str(
            self.id) + ", License: " + self.license_plate + ", Car type: " + self.make + ", " + self.model

    def __repr__(self):
        return str(self)


class ValidatorException(Exception):
    def __init__(self, message_list):
        self._messages = message_list

    def __str__(self):
        return str(self._messages)


"""
Java/C# - compiled languages

interface ICarValidator {
    public validate(Car c) throws ValidatorException; 
}

class CarValidatorRO implements ICarValidator {
}  


"""


class CarValidatorRO:
    def validate(self, car):
        """
        Validate car instance
        What to check for here:
            car id is an integer
            check license plate validity (list of counties is a module-level constant), apply rules from generate_cars

        :param car:
        :return: None
        :exception ValidatorException raised in case invalid car, exception stores ALL validation errors
        """
        if isinstance(car, Car) == False:
            # This should not appear in a working program
            raise ValidatorException(["Instance is not a car"])

        messages = []
        if car.id < 100 or car.id > 10 ** 5:
            messages.append("Invalid ID value")
        if str(car.id).isnumeric() is False:
            messages.append("Car ID is not numeric value")
        # License plate - counties
        tokens = car.license_plate.split(" ")
        if tokens[0] not in CAR_COUNTIES:
            messages.append("No such county")
        # TODO Some more checks required

        if len(messages) > 0:
            raise ValidatorException(messages)


class CarValidatorES:
    def validate(self, car):
        """
        Car validator for Spain
        :param car:
        :return:
        """
        pass


def generate_cars(n=10):
    """
    Generate n number of Car instances
    :param n:
    :return: List of Car instances

    id -> v1 (random integer between 100 and 100000) and check for duplicates
          v2 start from 100 and increment at each car
          [see German tank problem]

    license_plate -> (list of counties) + (random between 01 - 99) + (three random letters)

            (three random letters) -> v1 list of capital letters we select from
                                      v2 random integer between [65,90] for each of the three letters
    """
    data = list()
    for i in range(n):
        # TODO Implement this according to comments above
        # car = Car (...)
        # data.append(car)
        pass

    return data
