class ConsoleView:
    def __init__(self, controller):
        self.controller = controller

    def display_board(self):
        board = self.controller.board
        for row in board.grid:
            print("|" + "|".join(row) + "|")
        print(" " + " ".join(str(i) for i in range(board.columns)))

    def get_human_move(self):
        while True:
            try:
                column = int(input("Enter column (0-6): "))
                if 0 <= column < self.controller.board.columns:
                    return column
                else:
                    print("Invalid column. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 0 and 6.")

    def play_game(self):
        while True:
            self.display_board()
            if self.controller.current_player == self.controller.human_player:
                column = self.get_human_move()
                result = self.controller.human_move(column)
                if result == "Invalid":
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
                elif result == "No valid moves":
                    self.display_board()
                    print("No valid moves left. It's a draw!")
                    break



