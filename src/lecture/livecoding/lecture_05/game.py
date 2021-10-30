"""
    Functions for the Tic Tac Toe game go here
    These functions can call functions from board
    There is no UI ! (communicate with params / exceptions)No UI
"""
from board import board
from random import shuffle
from enum import Enum


class GameState(Enum):
    ONGOING = 0
    DRAW = 1
    WON = 2


class Game:
    def __init__(self):
        # TODO Make the computer strategy user-selectable
        self._board = board()
        self._strategy = MoveRandomStrategy()

    def get_state(self):
        if self._board.is_won():
            return GameState.WON
        if self._board.is_full():
            return GameState.DRAW
        return GameState.ONGOING

    def move_computer(self):
        """
        Alternate computer strategies (read strategy from a file ??)
        :param board:
        :return:
        """
        return self._strategy.move(self._board)

    # V1 Setter
    def get_board(self):
        return self._board

    # V2 property
    @property
    def board(self):
        return self._board


"""
    Strategy implementation below 
    Strategy design pattern - https://en.wikipedia.org/wiki/Strategy_pattern
"""

# interface IStrategy
# {
#     public Move move(Board b);
# }



class MoveFirstStrategy:
    def move(self, board):
        """
        The computer moves in the first square it finds available
        :param board: The game board
        :return: (x,y) of computer move
        """
        for row in range(3):
            for col in range(3):
                if board.get_pos(row, col) == 0:
                    return row, col
        raise ValueError("No moves available")


class MoveRandomStrategy:
    def move(self, board):
        """
        The computer moves in a random, but valid square.
        :param board:
        :return:
        """
        # TODO Computer wins if possible
        choices_choices = []
        for row in range(3):
            for col in range(3):
                if board.get_pos(row, col) == 0:
                    choices_choices.append((row, col))
        shuffle(choices_choices)
        return choices_choices[0]

# def move_computer_prevent_human_win(board):
#     """
#     The computer moves to prevent the human winning on the next move
#     :param board:
#     :return:
#     """
#     pass
