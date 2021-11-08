class CarRepository:
    def __init__(self):
        self._data = []

    def add(self, car):
        # TODO Check for ID duplicates
        self._data.append(car)

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


"""
    What to do for seminar 7
    1. Implement the generate_cars() function
    2. Implement the filter() function
    3. Generate 20 cars
    4. Add them to the repository
    5. Try out the filters!
"""
