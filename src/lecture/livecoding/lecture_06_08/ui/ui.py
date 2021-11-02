from lecture.livecoding.lecture_06_08.services.ingredientService import IngredientService
from lecture.livecoding.lecture_06_08.services.productService import ProductService
from lecture.livecoding.lecture_06_08.repo.repository import Repository


class UI:
    def __init__(self, ingredient_service, product_service):
        self.__ingr_service = ingredient_service
        self.__prod_service = product_service

    def start(self):
        print("menu")
