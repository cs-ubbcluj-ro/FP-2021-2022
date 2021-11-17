class Recipe:
    def __init__(self, _id, description, *required_stocks):
        # TODO Finish implementation for required stocks
        self._id = _id
        self._description = description
        self._required_stocks = required_stocks

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self._description

    @property
    def required_stocks(self):
        return self._required_stocks
