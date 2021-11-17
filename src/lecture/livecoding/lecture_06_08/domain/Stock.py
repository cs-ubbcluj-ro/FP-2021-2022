import unittest


class Stock:
    def __init__(self, ingredient, quantity):
        self._ingredient = ingredient
        self._quantity = quantity

    @property
    def ingredient(self):
        return self._ingredient

    @property
    def quantity(self):
        return self._quantity
