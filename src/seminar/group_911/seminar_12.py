import random
from texttable import Texttable


class Cell:
    def __init__(self):
        self._is_mined = False
        self._neighbour_mines = 0
        self._visible = False

    @property
    def mined(self):
        return self._is_mined

    @mined.setter
    def mined(self, value):
        self._is_mined = value

    @property
    def neighbours(self):
        return self._neighbour_mines

    @neighbours.setter
    def neighbours(self, value):
        self._neighbour_mines = value

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value

    def __str__(self):
        # if self.mined:
        #     return "X"
        if not self.visible:
            return "*"
        elif self.neighbours == 0:
            return ' '
        else:
            return str(self.neighbours)


class Minefield:
    def __init__(self, rows, cols, mines):
        self._rows = rows
        self._cols = cols
        self._mines = mines

        """
        (<no mines>, <is_visible>)
        0 - 8 -> number of adjacent mines
        -1 mine on the square
        """
        self._map = [[Cell() for i in range(self._cols)] for j in range(self._rows)]
        self._lay_mines(self._mines)

    def _lay_mines(self, mines):
        # TODO Better to have the list of available positions and select from them
        if mines == 0:
            return

        row = random.randint(0, self._rows - 1)
        col = random.randint(0, self._cols - 1)
        if not self._map[row][col].mined:
            self._map[row][col].mined = True
            '''
            Mark adjacent mines
            '''
            for i in range(max(row - 1, 0), min(row + 2, self._rows)):
                for j in range(max(col - 1, 0), min(col + 2, self._cols)):
                    self._map[i][j].neighbours += 1

            self._lay_mines(mines - 1)
        else:
            self._lay_mines(mines)

    def step(self, x, y):
        cell = self._map[x][y]
        if cell.mined:
            raise Exception("Game Over!")
        if cell.visible:
            return
        cell.visible = True
        if cell.neighbours > 0:
            return

        # Fill
        for i in range(max(x - 1, 0), min(x + 2, self._rows)):
            for j in range(max(y - 1, 0), min(y + 2, self._cols)):
                self.step(i, j)

    def is_cleared(self):
        for i in range(self._rows):
            for j in range(self._cols):
                if not self._map[i][j].visible and not self._map[i][j].mined:
                    return False
        return True

    def __str__(self):
        t = Texttable()

        header = list(range(self._cols))
        t.header(['/', ""] + header)

        for row in range(self._rows):
            t.add_row([str(row), "|"] + self._map[row])
        return t.draw()


minesweeper = Minefield(8, 10, 2)

while not minesweeper.is_cleared():
    print(minesweeper)
    x = input("Player step X=")
    y = input("Player step Y=")
    minesweeper.step(int(x), int(y))
