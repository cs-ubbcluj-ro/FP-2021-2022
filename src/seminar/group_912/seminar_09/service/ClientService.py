from seminar.group_912.seminar_09.domain.Client import Client
from seminar.group_912.seminar_09.service.UndoService import FunctionCall, Operation, CascadedOperation


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
        Record client deletion for undo/redo
        """
        fc_undo = FunctionCall(self.create, client.id, client.cnp, client.name)
        fc_redo = FunctionCall(self.delete, client.id)

        cope = CascadedOperation()
        cope.add(Operation(fc_undo, fc_redo))

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.getId(), False)
            """
            Record deleting rentals for undo/redo
            """
            fc_undo = FunctionCall(self._rental_service.create_rental, rent.id, rent.client, rent.car, rent.start,
                                   rent.end)
            fc_redo = FunctionCall(self._rental_service.delete_rental, rent.id)
            cope.add(Operation(fc_undo, fc_redo))

        self._undo_service.record_operation(cope)
        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
