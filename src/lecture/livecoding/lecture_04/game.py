"""
    Functions for the Tic Tac Toe game go here
    These functions can call functions from board
    There is no UI ! (communicate with params / exceptions)No UI
"""
from board import get_board_pos
from random import shuffle


def move_computer(board):
    """
    Alternate computer strategies (read strategy from a file ??)

    Strategy design pattern - https://en.wikipedia.org/wiki/Strategy_pattern

    :param board:
    :return:
    """
    # return move_computer_first_position(board)
    return move_computer_random_position(board)
    # move_computer_prevent_human_win(board)


def move_computer_first_position(board):
    """
    The computer moves in the first square it finds available
    :param board: The game board
    :return: (x,y) of computer move
    """
    for row in range(3):
        for col in range(3):
            if get_board_pos(board, row, col) == 0:
                return row, col
    raise ValueError("No moves available")


def move_computer_random_position(board):
    """
    The computer moves in a random, but valid square.
    :param board:
    :return:
    """
    # TODO Computer wins if possible
    choices_choices = []
    for row in range(3):
        for col in range(3):
            if get_board_pos(board, row, col) == 0:
                choices_choices.append((row, col))
    shuffle(choices_choices)
    return choices_choices[0]


def move_computer_prevent_human_win(board):
    """
    The computer moves to prevent the human winning on the next move
    :param board:
    :return:
    """
    pass
