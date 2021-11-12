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
