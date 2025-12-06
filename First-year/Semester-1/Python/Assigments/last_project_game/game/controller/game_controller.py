from game.model.board import Board
from game.model.player import Player

class GameController:
    def __init__(self):
        self.board = Board()
        self.human_player = Player("Human", 'X')
        self.computer_player = Player("Computer", 'O')
        self.current_player = self.human_player

    def switch_player(self):
        self.current_player = self.computer_player if self.current_player == self.human_player else self.human_player

    def human_move(self, column):
        if not self.board.is_valid_move(column):
            return "Invalid"
        row, col = self.board.make_move(column, self.human_player.token)
        if self.board.check_victory(self.human_player.token):
            return "Human wins"
        self.switch_player()
        return "Valid"

    def computer_move(self):
        # Simple strategy: block human or make a valid move
        for col in range(self.board.columns):
            if self.board.is_valid_move(col):
                row, _ = self.board.make_move(col, self.computer_player.token)
                if self.board.check_victory(self.computer_player.token):
                    return "Computer wins"
                self.board.grid[row][col] = ' '  # Undo move
        for col in range(self.board.columns):
            if self.board.is_valid_move(col):
                row, _ = self.board.make_move(col, self.human_player.token)
                if self.board.check_victory(self.human_player.token):
                    self.board.grid[row][col] = ' '  # Undo move
                    self.board.make_move(col, self.computer_player.token)
                    self.switch_player()
                    return "Valid"
                self.board.grid[row][col] = ' '  # Undo move
        for col in range(self.board.columns):
            if self.board.is_valid_move(col):
                self.board.make_move(col, self.computer_player.token)
                self.switch_player()
                return "Valid"
        return "No valid moves"
