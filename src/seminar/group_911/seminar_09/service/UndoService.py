class UndoService:
    """
    How can we implement multiple undo/redo with cascade?

    1. Keep track of program operations and reverse them (undo) / repeat them (redo)
        => Command design pattern
        (command = tell the program to do something, but later)

    2. Keep copies of repositories at each operation (deep-copy)
        => Memento design pattern (remember the state of the repos and restore them)
        (kinda like A34)

    3. State-diffing
        1. + 2.
    """

    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        self._history.append(operation)
        self._index = len(self._history) - 1

    def undo(self):
        if self._index == -1:
            # TODO Nice to have - UndoRedoException
            raise Exception("No more undos")
        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        pass


class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)


'''
    private ArrayList<Operation> history;
'''


class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class CascadedOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()


"""
Short example for undo/redo
def a(x, y, z):
    print(x, y, z)


def b(x, y, z, t, s):
    print(x, y, z, t, s)

call_a = Call(a, 97, 98, 99)
call_a.call()

call_b = Call(b, 97, 98, 99, 1001, 1002)
call_b.call()
"""
