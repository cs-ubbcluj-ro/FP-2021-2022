from seminar.group_917.seminar_09.domain.Client import Client
from seminar.group_917.seminar_09.service.UndoService import Call, Operation, ComplexOperation


class ClientService:
    def __init__(self, undo_service, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service
        self._undo_service = undo_service

    def create(self, client_id, client_cnp, client_name):
        client = Client(client_id, client_cnp, client_name)
        self._validator.validate(client)
        self._repository.store(client)
        return client

    def delete(self, client_id):
        """
            1. Delete the client
        """
        client = self._repository.delete(client_id)
        """
        undo -> repo.store(...)
        redo -> repo.delete(...)
        """
        # TODO Make sure you don't create object create/delete loops
        undo_call = Call(self._repository.store, client)
        redo_call = Call(self._repository.delete, client.id)

        operations_ur = []
        operations_ur.append(Operation(undo_call, redo_call))

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.id, False)
            # Operation for undo/redo
            redo_call = Call(self._rental_service.delete_rental, rent.id)
            undo_call = Call(self._rental_service.create_rental, rent.id, rent.client, rent.car, rent.start, rent.end)
            operations_ur.append(Operation(undo_call, redo_call))

        self._undo_service.record(ComplexOperation(operations_ur))
        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
