from seminar.group_917.seminar_06_09.domain.car import Car


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

    """
     The list of all cars in the car pool sorted by number of days they were rented.
    """

    def most_rented_cars(self):
        '''
        car_rental_days
            keys : cars
            values : number of days the car was rented for
        '''
        car_rental_days = {}

        """
        For each car
            - car_rental_days[car] = 0
            - go through the rentals list
            - calculate the number of days it was rented for  
                car_rental_days[car] += len(car_rental) 

        For each key,value in car_rental_days:
            - create a new instance of CarWithRentalDays
            - add it to the result list
            
        Sort the result list (some example code):
            rentals = []
            rentals.append(CarWithRentalDays(Car('100', 'CJ 11 WER', 'Dacia', 'Sandero', 'red'), 4))
            rentals.append(CarWithRentalDays(Car('101', 'CJ 11 WER', 'Dacia', 'Sandero', 'red'), 2))
            rentals.append(CarWithRentalDays(Car('102', 'CJ 11 WER', 'Dacia', 'Sandero', 'red'), 3))
            rentals.sort(key=lambda x: x.no_days, reverse=True)
            
            for r in rentals:
                print(r.car.id + " / " + str(r.no_days))
        """
        result = []
        # result.sort(key=no_days)
        result.sort(key=lambda car_days: car_days.no_days)

        pass

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


# def no_days(obj):
#     return obj.no_days


class CarWithRentalDays:
    """
    Data transfer object
        - we use it to move data between program layers
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
        # We use this to sort the list be number of rental days
        return self.no_days <= other.no_days
