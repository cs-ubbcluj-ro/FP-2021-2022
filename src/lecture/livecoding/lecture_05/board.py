"""
    Python Module description
    - Functions for board are here
    - These functions don't call other program modules
    - There is no UI ! (communicate with params / exceptions)
"""

"""
    Class = type, template, blueprint
    Object = class instance, takes up memory space
    
    
    class board exists at interpretation/compile time
    b exists at run time
"""


class board:
    def __init__(self):
        """
        __init__ -> Python constructor
        constructor = special method to build an object (class instance)
        At most 1 constructor per class

        C++
        Board* b = new Board(); // call Board constructor
        private/protected/public
        private = can access only inside of class
        public = can access from everywhere

        Python
        _  -> private (convention not to access from outside of class)
        __ -> private (Python name mangling, renames the field)
        start with a-z -> public
        """
        self.__data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get_pos(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("Position outside board")
        return self.__data[x][y]

    def set_pos(self, x, y, symbol):
        """
        Set an X or an O on the board
        :param x:
        :param y:
        :param symbol:
        :return:
        :except: raises ValueError is something is wrong
        """
        if not (symbol in ['X', 'O']):
            raise ValueError("Can only place X or O on board")
        if not (x in (0, 1, 2)) or not (y in (0, 1, 2)):
            raise ValueError("Move outside of board")
        if self.get_pos(x, y) != 0:
            raise ValueError("Cannot overwrite board")
        self.__data[x][y] = symbol

    def is_full(self):
        # TODO Count the number of symbols placed
        for row in range(3):
            for col in range(3):
                if self.get_pos(row, col) == 0:
                    # Found the first empty position => board not full
                    return False
        return True

    def is_won(self):
        # Is game won on a row
        for row in range(3):
            if self.get_pos(row, 0) in ['X', 'O'] and \
                    self.get_pos(row, 0) == self.get_pos(row, 1) == self.get_pos(row, 2):
                return True
        # Check on columns
        for col in range(3):
            if self.get_pos(0, col) in ['X', 'O'] and \
                    self.get_pos(0, col) == self.get_pos(1, col) == self.get_pos(2, col):
                return True

        # Check diagonals
        # Create an alias for the function, because why not !?
        gbp = self.get_pos
        if gbp(0, 0) in ['X', 'O'] and gbp(0, 0) == gbp(1, 1) == gbp(2, 2):
            return True
        # TODO Check second diagonal
        return False

    def __str__(self):
        """
        Convert board to str representation
        :param board:
        :return:
        """
        result = ""
        for row in range(3):
            for col in range(3):
                if self.get_pos(row, col) == 0:
                    result += '-'
                else:
                    result += self.get_pos(row, col)
            result += '\n'
        return result


if __name__ == "__main__":
    b = board()

    # b plays the role of self in get_pos
    pos = b.get_pos(2, 2)

    # alternate way of calling class member functions
    # b.get_pos(2, 2) <=> board.get_pos(b, 1, 2)
    # print(board.get_pos(b, 1, 2))

    b.set_pos(1, 1, 'X')
    b.set_pos(2, 2, 'O')
    print(b.is_won())
    print(b.get_pos(2, 2))

    # Not this
    # print(b.to_str())
    # THIS
    print(str(b))


def test_board():
    b = board()
    b.set_pos(1, 1, 'X')
    b.set_pos(0, 2, 'O')
    b.set_pos(2, 0, 'X')

    assert str(b) == '--O\n-X-\nX--\n', b
    assert b.is_full() is False
    assert b.is_won() is False

    # TODO Add a few more symbols and check again


test_board()
