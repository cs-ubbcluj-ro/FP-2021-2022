from lecture.livecoding.lecture_06_08.domain.IdObject import IdObject


class Recipe(IdObject):
    def __init__(self, _id, description, *required_stocks):
        # TODO Finish implementation for required stocks
        super().__init__(_id)
        self._description = description
        self._required_stocks = list(required_stocks)

    @property
    def description(self):
        return self._description

    @property
    def required_stocks(self):
        return self._required_stocks
