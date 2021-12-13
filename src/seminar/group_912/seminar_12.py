"""
Chomp game
    -> Field class
    -> Computer behaviour (strategy?)
    -> UI
"""
from texttable import Texttable
import random


class Field:
    def __init__(self, width, height):
        self._cols = width
        self._rows = height
        # 0 is default value
        self._data = [[0] * self._cols for i in range(self._rows)]

    def move(self, square, symbol):
        # Turn square into coordinates
        # TODO Only works up to Z (single letter for next line)
        col = ord(square[0]) - 65
        row = int(square[1:])
        self._move(row, col, symbol)
        pass

    def _move(self, x, y, symbol):
        """
        Make a move on the board
        :param x: Row
        :param y: Column
        :param symbol: Player sign (X or O)
        """
        if x == 0 and y == 0:
            raise Exception("Game Over!")

        if not (0 <= x < self._rows and 0 <= y < self._cols):
            raise Exception("Not a valid cell!")

        if self._data[x][y] != 0:
            raise Exception("Cell already taken!")

        for i in range(x, self._rows):
            for j in range(y, self._cols):
                if self._data[i][j] == 0:
                    self._data[i][j] = symbol

    def empty_squares(self):
        """
        Return a list of all non-played squares (without (0,0))
        :return:
        """
        result = []
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] == 0:
                    result.append((i, j))
        # Removes the (0,0), which is the first element in the list
        result.pop(0)
        return result

    def is_full(self):
        """
        True if and only if only available move is at (0,0)
        :return:
        """
        return self._data[0][1] != 0 and self._data[1][0] != 0

    def __str__(self):
        t = Texttable()

        # Horizontal header
        header_row = ['/']
        for i in range(self._cols):
            header_row.append(chr(65 + i))
        t.header(header_row)

        for i in range(self._rows):
            row = self._data[i]
            # Initialize vertical header
            display_row = [i]

            for j in range(self._cols):
                val = self._data[i][j]
                if val == 0:
                    if i == 0 and j == 0:
                        display_row.append('*')
                    else:
                        display_row.append(' ')
                else:
                    display_row.append(val)

            t.add_row(display_row)
        return t.draw()


class ComputerPlayer():
    def move(self, field):
        """
        The computer player moves
        :param field: The playing field
        :return: The location played by the computer
        """
        square = field.empty_squares()[0]
        # Convert (1,1) to A1
        return chr(square[1] + 65) + str(square[0])


class ComputerPlayerRandom():
    def move(self, field):
        """
        The computer player moves
        :param field: The playing field
        :return: The location played by the computer
        """
        square = random.choice(field.empty_squares())
        # Convert (1,1) to A1
        return chr(square[1] + 65) + str(square[0])


class ComputerPlayerAlmostRandom:
    def move(self, field):
        """
        The computer player moves
        :param field: The playing field
        :return: The location played by the computer
        """
        squares = field.empty_squares()
        square = None

        if (0, 1) in squares and not (1, 0) in squares:
            square = (0, 1)
        elif (1, 0) in squares and not (0, 1) in squares:
            square = (1, 0)
        else:
            square = squares[-1]
        # Convert (1,1) to A1
        return chr(square[1] + 65) + str(square[0])


class UI:
    def __init__(self):
        # TODO Field size and computer level can be read from UI or a settings file
        self._field = Field(5, 4)
        self._ai = ComputerPlayerAlmostRandom()

    def start(self):
        print("Welcome to Chomp!")

        player_turn = True
        while not self._field.is_full():
            print(str(self._field))

            if player_turn:
                # TODO Some validation here
                move = input("Enter your move: ")
                self._field.move(move, 'X')
            else:
                ai_move = self._ai.move(self._field)
                print("Computer moves at " + str(ai_move))
                self._field.move(ai_move, 'O')
            player_turn = not player_turn

        if player_turn:
            print("You LOST!")
        else:
            print("You WON!")


ui = UI()
ui.start()
