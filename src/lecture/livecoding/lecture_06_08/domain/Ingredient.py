import unittest

from lecture.livecoding.lecture_06_08.domain.IdObject import IdObject


class Ingredient(IdObject):
    """
    - id, description, stock (default in grams), expiration date
    """

    def __init__(self, _id, description="n/a"):
        # TODO Add expiration date
        super().__init__(_id)
        self.__description = description

    @property
    def description(self):
        return self.__description
