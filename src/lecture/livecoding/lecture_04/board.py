"""
    Python Module description
    - Functions for board are here
    - These functions don't call other program modules
    - There is no UI ! (communicate with params / exceptions)
"""


def init_board():
    """
    Start up a game board (3x3, empty)

    'X' -> 'X'
    'O' -> 'O' (represent using uppercase chars)

    :return: New board
    """
    # TODO Also try with a for loop [0] * 3, [ [0 for i in range(3)] * 3 ]
    # TODO Represent as a single list, with 1 == X, -1 == O (then abs(sum(row)) == 3)

    # TODO Better board representation for checks
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def get_board_pos(board, x, y):
    return board[x][y]


def set_board_pos(board, x, y, symbol):
    """
    Set an X or an O on the board
    :param board:
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
    if get_board_pos(board, x, y) != 0:
        raise ValueError("Cannot overwrite board")
    board[x][y] = symbol


def is_board_full(board):
    # TODO Count the number of symbols placed
    for row in range(3):
        for col in range(3):
            if get_board_pos(board, row, col) == 0:
                # Found the first empty position => board not full
                return False
    return True


def is_board_won(board):
    # Is game won on a row
    for row in range(3):
        if get_board_pos(board, row, 0) in ['X', 'O'] and \
                get_board_pos(board, row, 0) == get_board_pos(board, row, 1) == get_board_pos(board, row, 2):
            return True
    # Check on columns
    for col in range(3):
        if get_board_pos(board, 0, col) in ['X', 'O'] and \
                get_board_pos(board, 0, col) == get_board_pos(board, 1, col) == get_board_pos(board, 2, col):
            return True

    # Check diagonals
    # Create an alias for the function, because why not !?
    gbp = get_board_pos
    if gbp(board, 0, 0) in ['X', 'O'] and gbp(board, 0, 0) == gbp(board, 1, 1) == gbp(board, 2, 2):
        return True
    # TODO Check second diagonal
    return False


def to_str(board):
    """
    Convert board to str representation
    :param board:
    :return:
    """
    result = ""
    for row in range(3):
        for col in range(3):
            if get_board_pos(board, row, col) == 0:
                result += '-'
            else:
                result += get_board_pos(board, row, col)
        result += '\n'
    return result


def test_board():
    b = init_board()
    set_board_pos(b, 1, 1, 'X')
    set_board_pos(b, 0, 2, 'O')
    set_board_pos(b, 2, 0, 'X')

    assert to_str(b) == '--O\n-X-\nX--\n', b
    assert is_board_full(b) == False
    assert is_board_won(b) == False

    # TODO Add a few more symbols and check again


test_board()
