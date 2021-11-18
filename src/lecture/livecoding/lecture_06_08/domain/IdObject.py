class IdObject:
    def __init__(self, _id):
        self._id = _id

    @property
    def id(self):
        return self._id
