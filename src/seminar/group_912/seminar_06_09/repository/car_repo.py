from seminar.group_912.seminar_06_09.repository.repository_exception import RepositoryException


class CarRepository:
    # TODO Finish implementation
    def __init__(self):
        self._data = {}

    def add(self, car):
        if car.id in self._data.keys():
            raise RepositoryException("Duplicate Car id")
        self._data[car.id] = car

    def filter(self, license=None, make=None, model=None, color=None):
        """
        Filter cars by their parameters

        e.g.
        repo.filter()
        repo.filter(color='red')
        repo.filter(color='black',make = 'Audi')
        repo.filter(make = 'Skoda',model='Fabia')
        repo.filter(license='CJ 01 ABC',make = 'Skoda',model='Fabia',color='blue')

        Implementation
            - ignore all fields that are None
            - filter by those which are not None


        :param license:
        :param make:
        :param model:
        :param color:
        :return: List of filtered cars
        """

        result = []
        for car in self._data:
            # TODO Check that car passes filter
            # result.append(car)
            pass

        return result
