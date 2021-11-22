class UndoService:
    """
    1. Command design pattern
        -> tell the computer what to do (call a method), but not to do it now, but sometime later
        (store the command and call it when it's needed)

    2. Memento design pattern
        -> Keep a copy of the program's (entity's etc.) previous state(s) and restore to it when needed
    """

    def __init__(self):
        # History of program operations
        self._history = []
        # Where are we in the operation history
        self._index = -1

    def undo(self):
        pass

    def redo(self):
        pass

    def record(self, operation):
        """
        Record operation for undo/redo
        :param operation:
        :return:
        """
        pass


class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class ComplexOperation:
    def __init__(self, *operation):
        self._operations = operation

    def undo(self):
        for operation in self._operations:
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()


class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        # TODO Unpack parameters?
        self._function_name(self._function_params)
