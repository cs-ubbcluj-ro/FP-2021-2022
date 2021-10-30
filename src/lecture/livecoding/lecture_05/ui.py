"""
    Tic Tac Toe ui!
    Can call functions from game/board
    All input/print statements go here

    A few problems with modular Tic Tac Toe
        1. All functions are exposed ("public") and can be called at any time
        2. We don't have any custom types defined (our board is a Python list)
        3. We can modify the board in unexpected ways -> board[1][1] = 'A'
        4. Some params have to carried around (e.g. board)
        5. We can't use many of Python's inbuilt functions (e.g. to_str(board) vs. str(board))
"""
# import board
from board import board
from game import Game, GameState


class GameUI:
    def __init__(self):
        self._game = Game()

    def _read_position(self):
        x = int(input("X="))
        y = int(input("Y="))
        return x, y

    def start(self):
        is_human_turn = True

        while self._game.get_state() == GameState.ONGOING:
            print("Game board:")
            # V1 - board getter
            # print(str(self._game.get_board()))
            # V2 - board property
            print(str(self._game.board))

            try:
                if is_human_turn:
                    x, y = self._read_position()
                    self._game.board.set_pos(x, y, 'X')
                else:
                    x, y = self._game.move_computer()
                    # TODO Should be moved into game
                    self._game.board.set_pos(x, y, 'O')
                    print("Computer moves (" + str(x) + "," + str(y) + ")")
                is_human_turn = not is_human_turn
            except ValueError as ve:
                print(str(ve))

        if self._game.get_state() == GameState.WON:
            if is_human_turn:
                # Var is flipped after the last move was made
                print("Computer wins!")
            else:
                print("You win!")
            print(str(self._game.board))
        else:
            print("It's a draw!")

print(__name__)
ui = GameUI()
ui.start()
