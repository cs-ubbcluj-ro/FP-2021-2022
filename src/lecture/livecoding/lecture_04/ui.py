"""
    Tic Tac Toe ui!
    Can call functions from game/board
    All input/print statements go here
"""
# import board
from board import init_board, to_str, is_board_full, is_board_won, set_board_pos
from game import move_computer


def read_position():
    x = int(input("X="))
    y = int(input("Y="))
    return x, y


def start():
    board = init_board()

    is_human_turn = True

    while not is_board_won(board) and not is_board_full(board):
        print("Game board:")
        print(to_str(board))

        try:
            if is_human_turn:
                x, y = read_position()
                set_board_pos(board, x, y, 'X')
            else:
                x, y = move_computer(board)
                set_board_pos(board, x, y, 'O')
                print("Computer moves (" + str(x) + "," + str(y) + ")")
            is_human_turn = not is_human_turn
        except ValueError as ve:
            print(str(ve))

    if is_board_won(board):
        if is_human_turn:
            # Var is flipped after the last move was made
            print("Computer wins!")
        else:
            print("You win!")
        print(to_str(board))
    else:
        print("It's a draw!")


start()
