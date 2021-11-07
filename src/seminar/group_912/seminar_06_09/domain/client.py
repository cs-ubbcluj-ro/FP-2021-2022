class Client:
    def __init__(self, client_id, cnp, name):
        self._clientId = client_id
        self._cnp = cnp
        self._name = name

    @property
    def id(self):
        return self._clientId

    @property
    def cnp(self):
        return self._cnp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __eq__(self, z):
        if isinstance(z, Client) is False:
            return False
        return self.id == z.id

    def __str__(self):
        return "Id=" + str(self.id) + ", Name=" + str(self.name)

    def __repr__(self):
        return str(self)
