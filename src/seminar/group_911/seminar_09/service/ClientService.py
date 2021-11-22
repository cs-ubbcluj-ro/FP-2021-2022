from seminar.group_911.seminar_09.domain.Client import Client
from seminar.group_911.seminar_09.service.UndoService import Call, CascadedOperation
from seminar.group_912.seminar_09.service.UndoService import Operation


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
        client, rentals = self._delete(client_id)
        """
            2. Support for undo/redo

            How do we get rid of undo-calls creating their own undo entries?
                1. Separate private method without creating operation
                2. Suspend recording operations in UndoService during undo call

        """
        undo_call = Call(self.create, client.id, client.cnp, client.name)
        redo_call = Call(self._delete, client.id)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        """
        Add all rentals to cascaded operation
        """
        for rent in rentals:
            # TODO Make sure rental service functions don't lead to an undo loop
            undo_call = Call(self._rental_service.create_rental, rent.id, rent.client, rent.car, rent.start, rent.end)
            redo_call = Call(self._rental_service.delete_rental, rent.id)
            cope.add(Operation(undo_call, redo_call))

        self._undo_service.record(cope)
        return client

    def _delete(self, client_id):
        """
            1. Delete the client
        """
        client = self._repository.delete(client_id)

        '''
            3. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.getId(), False)

        return client, rentals

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
