from board import Board
from ui import Ui

if __name__ == "__main__":
    board = Board()
    ui = Ui(board)
    ui.gameplay()