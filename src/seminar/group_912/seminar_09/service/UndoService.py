class UndoService:
    """
    How to implement multiple undo/redo with cascading?

    1. Memento design pattern (memento = sticky note)
        - keep the state of the objects and restore them when appropriate
        - can be very memory inefficient

    2. Command design pattern
        - remember the operations and execute them when appropriate (= command)
        - memory-efficient, but probably more complex
    """

    def __init__(self):
        # History of operations for undo/redo
        self._history = []  # ArrayList<Operation> history; -> Java,C++,C#
        # Our current position in undo/redo
        self._index = -1
        # Setting this to false stops recording operations for undo/redo
        self._record_flag = True

    def record_operation(self, operation):
        # TODO Implement this
        if self._record_flag is False:
            return
        pass

    def undo(self):
        # TODO Implement this
        self._record_flag = False
        pass
        # ... do somethig ...
        self._record_flag = True

    def redo(self):
        # TODO Implement this
        pass


class Operation:
    def __init__(self, function_undo, function_redo):
        self._function_undo = function_undo
        self._function_redo = function_redo

    def undo(self):
        self._function_undo.call()

    def redo(self):
        self._function_redo


class CascadedOperation(Operation):
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for oper in self._operation:
            oper.undo()

    def redo(self):
        for oper in self._operation:
            oper.redo()


class FunctionCall:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)


"""
Example for FunctionCall

def a(a, b, c):
    print(a, b, c)


def b(a, b, c, d, e):
    print(a, b, c, d, e)

fc_undo = FunctionCall(a, 10, 11, 12)
# fc_undo.call()

fc_redo = FunctionCall(b, 10, 11, 12, 89, 98)
# fc.call()
op = Operation(fc_undo, fc_redo)
op.undo()
"""
