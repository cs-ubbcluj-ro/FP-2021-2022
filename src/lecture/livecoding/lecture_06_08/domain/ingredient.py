class Ingredient:
    """
    - id, description, stock (default in grams), expiration date
    """

    def __init__(self, _id, description="n/a", stock=0):
        """
        Create a new ingredient
        :param _id:
        :param description:
        :param stock:
        """
        self.__id = _id
        self.__description = description
        self.stock = stock

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock must be >= 0")
        self.__stock = new_stock


def test_ingredient():
    ingr = Ingredient(100, "White flour 550", 10)
    assert ingr.id == 100
    assert ingr.description == "White flour 550"
    assert ingr.stock == 10

    try:
        ingr.stock -= 100
        # Test must fail if the exception was not raised
        assert False
    except ValueError as ve:
        assert str(ve) == "Stock must be >= 0"

    try:
        ingr = Ingredient(100, "White flour 550", -10)
        # Test must fail if the exception was not raised
        assert False
    except ValueError as ve:
        assert str(ve) == "Stock must be >= 0"


test_ingredient()
