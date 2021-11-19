class Address:
    """
      Represent an address
    """

    def __init__(self, street, nr, city):
        self._street = street
        self._nr = nr
        self._city = city

    @property
    def street(self):
        return self._street

    @property
    def number(self):
        return self._nr

    @property
    def city(self):
        return self._city

    def __str__(self):
        """
          Give a string representation for the address
          return string
        """
        return self._street + " nr." + self._nr + " " + self._city


class Student:
    """
      Represent a student
    """

    def __init__(self, id, name, adr):
        """
         Create a new student
         id, name String
         address - Address
        """
        self.__id = id
        self.__name = name
        self.__adr = adr

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__adr

    def __str__(self):
        """
          Give a string representation for the student
          return string
        """
        return self.__id + " " + self.__name + " " + str(self.__adr)

    def __eq__(self, ot):
        """
          Define equal for students
          ot - student
          return True if ot and the current instance represent the same student
        """
        if isinstance(ot, Student) is False:
            return False
        return self.__id == ot.__id
