class Ingredient:
    """
    - id, description, stock (default in grams), expiration date
    """

    def __init__(self, _id, description="n/a"):
        # TODO Add expiration date
        self.__id = _id
        self.__description = description

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description
