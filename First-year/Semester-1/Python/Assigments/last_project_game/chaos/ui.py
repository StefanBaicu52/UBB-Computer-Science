from chaos.board import Board
from chaos.console import GameController
import texttable as tt



class UI:
    def __init__(self,controller):
        self.controller = controller

    def display_board(self):
        board = self.controller.board
        table = tt.Texttable()

        # Add each row to the table
        for row in board.grid:
            table.add_row(row)

        # Set alignment and formatting (optional)
        table.set_cols_align(["c"] * len(board.grid[0]))  # Center align all columns
        table.set_deco(tt.Texttable.HEADER | tt.Texttable.VLINES | tt.Texttable.HLINES)

        # Print the table
        print(table.draw())

    def get_human_move(self):
        while True:
            try:
                column=int(input("Enter a column: "))
                row=int(input("Enter a row: "))
                if row < 0 or row > 5 or column < 0 or column > 5:
                    raise ValueError("Invalid input! Row and column must be between 0 and 5 (inclusive).")
                if not self.controller.board.valid_move(row,column):
                    raise ValueError("Invalid move")
                else:
                    return row,column
            except ValueError:
                print("Invalid input. Enter a number between 0 and 5.")

    def play_game(self):
        while True:
            self.display_board()
            if self.controller.current_player==self.controller.human_player:
                row,column = self.get_human_move()
                result = self.controller.human_move(row,column)
                if result == "Invalid move":
                    print("Invalid move. Try again.")
                elif result == "Human wins":
                    self.display_board()
                    print("Human wins!")
                    break
            else:
                result = self.controller.computer_move()
                if result == "Computer wins":
                    self.display_board()
                    print("Computer wins!")
                    break

if __name__ == "__main__":
    controller = GameController()
    ui = UI(controller)
    ui.play_game()
