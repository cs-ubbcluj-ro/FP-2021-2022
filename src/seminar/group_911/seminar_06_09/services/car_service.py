from seminar.group_911.seminar_06_09.domain.car import Car


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
    Statistics
     The list of all cars in the car pool sorted by number of days they were rented.
    
    What are the required steps to implement this statistics?
        Iterate over all the rentals:
            Increase the rental length for the car in the current rental
            [store this info in a dictionary]
            
        Transform the dict into a list in order to sort
        Sort the list 
        Return to calling function
    """

    def most_rented_cars(self):
        '''
        Start working with a dictionary
        '''
        car_days_dict = {}
        for rental in self._rental_service.filter_rentals(None, None):
            if rental.car not in car_days_dict:
                car_days_dict[rental.car] = len(rental)
            else:
                car_days_dict[rental.car] += len(rental)
        # Also add card that were never rented
        for car in self._repository:  # look at __iter__, __next__
            if car not in car_days_dict:
                car_days_dict[car] = 0  # car has 0 rental days

        '''
        Transform to a list that will reach the calling function
        '''
        result = []
        for car in car_days_dict:
            result.append(CarRentalDaysDTO(car, car_days_dict[car]))

        """
        Sort the list in decreasing order before returning
        
        lambda
            - exists in many programming languages
            - anonymous function => its called in the same place where it is defined
            - usual to write small, one-liners
        """
        result.sort(key=lambda x: x.no_days, reverse=True)

        '''
        1. sort by length of rental (low priority)
        2. sort by amount of income (high priority)
            => sort algorithm stability
        '''


        return result

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


class CarRentalDaysDTO:
    """
    Data transfer object (DTO) for a car and a number of rental days
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
        """
        This allows sorting CarRentalDaysDTO objects using the <= operator
        """
        return self.no_days < other.no_days
