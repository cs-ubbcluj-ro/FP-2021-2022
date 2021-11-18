from lecture.livecoding.lecture_06_08.domain.IdObject import IdObject
from lecture.livecoding.lecture_06_08.repo.repository import Repository


class Product(IdObject):
    def __init__(self, _id, recipe):
        super().__init__(_id)
        self._recipe = recipe

    @property
    def recipe(self):
        return self._recipe
