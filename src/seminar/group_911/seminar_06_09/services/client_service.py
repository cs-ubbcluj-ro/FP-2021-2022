from seminar.group_911.seminar_06_09.domain.client import Client


class ClientService:
    def __init__(self, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service

    def create(self, client_id, client_cnp, client_name):
        client = Client(client_id, client_cnp, client_name)
        self._validator.validate(client)
        self._repository.add(client)
        return client

    def delete(self, client_id):
        """
            1. Delete the client
        """
        client = self._repository.delete(client_id)

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.id, False)

        return client
