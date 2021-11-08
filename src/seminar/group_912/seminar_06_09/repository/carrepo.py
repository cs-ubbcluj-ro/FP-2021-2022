class CarRepository:
    def __init__(self):
        """
        Initialize the repository
        """
        # TODO Implement
        self._data = []

    def add(self, car):
        """
        Add car to the repository
        :param car:
        :return:
        :exception: Raise RepoException in case duplicate license plates
        """
        # TODO Implement
        pass

    def filter(self, license_plate, make, model, color):
        """
        Return the list of cars which pass the provided filter(s)

        if parameter values is None -> disregard it
        parameter values is not None -> filter by it

        e.g.
        repo.filter(color='red')
        repo.filter(color='black', make='Renault')
        repo.filter(license_plate='CJ 10 QWE',make='Renault')

        Implementation ?
        Loop over all the cars
            For each car, check which function argument is not None
                Use 'continue' keyword to move to next car when mismatch
        """
        filtered_list = []
        for car in self._data:
            # TODO Does the car pass the filter?
            # filtered_list.append(car)
            pass

        return filtered_list


# TODO what to do for seminar 7
"""
    1. Generate 50 cars (generate_cars)
    2. filter them in the repo (repo.filter)
    3. print out filtered list
"""
