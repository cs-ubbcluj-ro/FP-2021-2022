from texttable import Texttable
import random


class Minefield:
    def __init__(self, width, height, mines):
        self._width = width
        self._height = height
        self._mines = mines

        """
        Data representation
            0 for starters
            number in a tile = number of adjacent mines
            -1 = tile is a mine
        """
        self._field = [[0 for i in range(self._width)] for j in range(self._height)]

        self._lay_mines()

    def click(self, row, col):
        # TODO Bound checks
        if self._field[row][col] == -1:
            raise Exception("Game Over!")

        # Mark the square as visible
        self._field[row][col] += 10

        # TODO Refactor the code below
        # Square has no adjacent mines
        if self._field[row][col] == 10:
            # Recursively reveal adjacent squares
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    if 0 <= x < self._height:
                        if 0 <= y < self._width:
                            if x != row or y != col:
                                if self._field[x][y] < 10:
                                    self.click(x, y)

    def _lay_mines(self):
        # Build list of valid tiles
        tiles = []
        for i in range(self._width):
            for j in range(self._height):
                tiles.append((i, j))
        # Pick random mined tiles
        random.shuffle(tiles)

        # Lay the mines
        for m in tiles[:self._mines]:
            row = m[1]
            col = m[0]
            # Add the mine to the field
            self._field[row][col] = -1
            # Increase the number of mines in all adjacent squares
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    if 0 <= x < self._height:
                        if 0 <= y < self._width:
                            if self._field[x][y] != -1:
                                self._field[x][y] += 1

    def __str__(self):
        header = []
        for letter in range(self._width):
            header.append(chr(65 + letter))
        header.append('X')

        t = Texttable()
        t.header(header)
        for i in range(self._height):
            vis_array = []
            for j in range(self._width):
                sq = self._field[i][j]

                if sq == 10:
                    # empty square
                    vis_array.append(' ')
                if sq > 10:
                    # mined square
                    vis_array.append(sq - 10)
                if sq < 10:
                    vis_array.append('*')
            t.add_row(vis_array + [i])
        return t.draw()


minesweeper = Minefield(10, 8, 3)
# print(str(minesweeper))
minesweeper.click(0, 0)
print(str(minesweeper))
# minesweeper.click('B5')
