from lecture.livecoding.lecture_06_08.repo.repository import Repository


class IngredientService:
    # TODO Fill in this skeleton class
    def __init__(self, ingredient_repo):
        self.__repo = ingredient_repo

    def add_ingredient(self, ingredient):
        self.__repo.add(ingredient)
