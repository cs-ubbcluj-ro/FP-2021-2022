from lecture.livecoding.lecture_06_08.repo.repository import Repository


class ProductService:
    # TODO Fill in this skeleton class
    def __init__(self, product_repo):
        self.__repo = product_repo

    def add_product(self, product):
        self.__repo.add(product)
