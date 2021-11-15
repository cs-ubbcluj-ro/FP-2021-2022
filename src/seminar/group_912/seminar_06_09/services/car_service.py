from seminar.group_912.seminar_06_09.domain.car import Car


class CarService:
    def __init__(self, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service

    def create(self, car_id, license_plate, car_make, car_model, car_color):
        car = Car(car_id, license_plate, car_make, car_model, car_color)
        self._validator.validate(car)
        self._repository.add(car)
        return car

    def delete(self, car_id):
        """
            1. Delete the car from the repository
        """
        car = self._repository.delete(car_id)

        '''
            2. Delete its rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(None, car)
        for rent in rentals:
            self._rental_service.delete_rental(rent.id, False)
        return car

    """
        Statistics
         The list of all cars in the car pool sorted by number of days they were rented
    """

    def most_rented_cars(self):
        cars_rentals_dict = {}
        """
        What do we need to do?

        For each car
            - count the number of days it was rented for 
                cars_rentals_dict[car] = 0 # initialize car that is not (yet) rented
                ...
                cars_rentals_dict[car] += len(car_rental) # add the number of days of current rental

        Transform the dict into a list so we can move it into the UI
        
        Sort this list
            result = []
            result.append(CarDayCountDTO(Car('102', 'CJ 10 TOY', 'Toyota', 'RAV4', 'blue'), 5))
            result.append(CarDayCountDTO(Car('103', 'CJ 10 TOY', 'Toyota', 'RAV4', 'blue'), 2))
            result.append(CarDayCountDTO(Car('104', 'CJ 10 TOY', 'Toyota', 'RAV4', 'blue'), 7))
            result.sort(key=lambda x: x.no_days, reverse=True)
            for dto in result:
                print(dto.car.id, dto.no_days)
        
        Return it
        
        :return:
        """
        pass


class CarDayCountDTO:
    """
    Data transfer object that holds a car and a day count
    """

    def __init__(self, car, no_days):
        self._car = car
        self._no_days = no_days

    @property
    def car(self):
        return self._car

    @property
    def no_days(self):
        return self._no_days

    def __le__(self, other):
        return self.no_days < other.no_days
