from chaos.board import Board
from chaos.console import GameController
import texttable as tt


class UI:
    def __init__(self, controller):
        self.controller = controller

    def display_board(self):
        board = self.controller.board
        table = tt.Texttable()

        for row in board.grid:
            table.add_row(row)

        table.set_cols_align(["c"] * len(board.grid[0]))
        table.set_deco(tt.Texttable.HEADER | tt.Texttable.VLINES | tt.Texttable.HLINES)

        board_output = table.draw()
        print(board_output)

        # Salvăm tabla de joc într-un fișier
        with open("game_board.txt", "w") as file:
            file.write(board_output)

    def get_human_move(self):
        while True:
            try:
                user_input = input("Enter row and column (e.g., 0 2): ").strip()
                row, col = map(int, user_input.split())
                if row not in range(3) or col not in range(3):
                    raise ValueError("Row and column must be between 0 and 2.")
                return row, col
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 2, separated by a space.")

    def play_game(self):
        prev_phase = self.controller.placement_phase
        while True:
            self.display_board()

            if not self.controller.placement_phase and prev_phase:
                print("\n--- Placement phase is over. Now you can move your pieces! ---\n")
            prev_phase = self.controller.placement_phase

            if self.controller.placement_phase:
                if self.controller.current_player == self.controller.human_player:
                    row, col = self.get_human_move()
                    try:
                        result = self.controller.human_move(row, col)
                    except ValueError as e:
                        print(f"Invalid move: {e}")
                        continue  # Retry if invalid
                else:
                    result = self.controller.computer_move()
            else:
                if self.controller.current_player == self.controller.human_player:
                    while True:
                        print("Select a piece to move:")
                        from_row, from_col = self.get_human_move()
                        if self.controller.board.grid[from_row][from_col] == self.controller.human_player.token:
                            break
                        print("Invalid selection. Choose one of your own pieces.")

                    while True:
                        print("Select a destination:")
                        to_row, to_col = self.get_human_move()
                        try:
                            result = self.controller.move_piece(from_row, from_col, to_row, to_col)
                            break  # Exit loop if valid move
                        except ValueError as e:
                            print(f"Invalid move: {e}. Try again.")

                else:
                    result = self.controller.computer_move()

            if result in ["Human wins", "Computer wins"]:
                self.display_board()
                print(result)
                break


if __name__ == "__main__":
    controller = GameController("X", "O")  # Inițializăm un board gol doar pentru afișare
    ui = UI(controller)
    ui.display_board()  # 🔹 Afișăm tabla de joc goală înainte de a alege simbolul

    while True:
        human_token = input("Choose your token (X or O): ").upper()
        if human_token in ["X", "O"]:
            break
        print("Invalid choice. Please choose X or O.")

    computer_token = "O" if human_token == "X" else "X"
    controller = GameController(human_token, computer_token)  # Creăm un nou controller cu simbolurile corecte
    ui = UI(controller)
    ui.play_game()
