class Product:
    def __init__(self, _id, recipe):
        self._id = _id
        self._recipe = recipe

    @property
    def id(self):
        return self.__id

    @property
    def recipe(self):
        return self._recipe
