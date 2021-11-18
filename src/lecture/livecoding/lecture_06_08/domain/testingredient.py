import unittest

from lecture.livecoding.lecture_06_08.domain.Ingredient import Ingredient


class IngredientTest(unittest.TestCase):
    def test_ingredient(self):
        ingr = Ingredient(103, "Salt (regular)")
        self.assertEqual(ingr.id, 103)
        self.assertEqual(ingr.description, "Salt (regular)")
