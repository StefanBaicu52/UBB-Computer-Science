from chaos.board import Board
from chaos.player import Player
import random

class GameController:
    def __init__(self, human_token, computer_token):
        self.board = Board()
        self.human_player = Player("Human", human_token)
        self.computer_player = Player("Computer", computer_token)
        self.current_player = self.human_player
        self.placement_phase = True
        self.human_pieces_placed = 0
        self.computer_pieces_placed = 0

    def switch_player(self):
        self.current_player = (
            self.human_player if self.current_player == self.computer_player else self.computer_player
        )

    def human_move(self, row, column):
        if self.placement_phase:
            if self.human_pieces_placed < 4:
                if self.board.valid_move(row, column, placement_phase=True):
                    self.board.make_move(row, column, self.human_player.token)
                    self.human_pieces_placed += 1
                    if self.board.check_victory(self.human_player.token):
                        return "Human wins"
                    self.switch_player()
                    if self.human_pieces_placed == 4 and self.computer_pieces_placed == 4:
                        self.placement_phase = False  # Se trece la faza de mișcare
                    return "Valid"
                else:
                    raise ValueError("Invalid move. Position already occupied.")
        else:
            raise ValueError("Use move_piece in movement phase.")

    def move_piece(self, from_row, from_col, to_row, to_col):
        if not self.placement_phase:
            if self.board.grid[from_row][from_col] == self.current_player.token:
                # ✅ Nu mai verificăm dacă mutarea este adiacentă!
                self.board.move_piece(from_row, from_col, to_row, to_col)
                if self.board.check_victory(self.current_player.token):
                    return f"{self.current_player.name} wins"
                self.switch_player()
                return "Valid move"
            else:
                raise ValueError("Invalid move. Can only move your own piece.")
        else:
            raise ValueError("Cannot move pieces during placement phase.")

    def computer_move(self):
        if self.placement_phase:
            if self.computer_pieces_placed < 4:
                block_move = self.block_human_win()

                if block_move:
                    # If there's a blocking move, the computer makes it
                    row, col = block_move
                    self.board.make_move(row, col, self.computer_player.token)
                else:
                    # Place in a random valid empty cell
                    empty_cells = [
                        (r, c) for r in range(self.board.rows) for c in range(self.board.cols)
                        if self.board.valid_move(r, c, placement_phase=True)
                    ]
                    if empty_cells:
                        row, col = random.choice(empty_cells)
                        self.board.make_move(row, col, self.computer_player.token)

                # Increment the pieces placed counter
                self.computer_pieces_placed += 1

                # Check for victory after placing a piece
                if self.board.check_victory(self.computer_player.token):
                    return "Computer wins"

                # Switch to the human player's turn
                self.switch_player()

            # Transition to movement phase if both players have placed 4 pieces
            if self.human_pieces_placed == 4 and self.computer_pieces_placed == 4:
                self.placement_phase = False  # Transition to movement phase
                print("Transitioning to movement phase")  # Debug message
        else:
            # Movement phase logic
            movable_pieces = [
                (r, c) for r in range(self.board.rows) for c in range(self.board.cols)
                if self.board.grid[r][c] == self.computer_player.token
            ]
            random.shuffle(movable_pieces)
            for from_row, from_col in movable_pieces:
                empty_cells = [
                    (r, c) for r in range(self.board.rows) for c in range(self.board.cols)
                    if self.board.grid[r][c] == ' '
                ]
                if empty_cells:
                    to_row, to_col = random.choice(empty_cells)
                    return self.move_piece(from_row, from_col, to_row, to_col)

        return "No valid moves"

    def block_human_win(self):
        """Verifică dacă există o mutare câștigătoare pentru jucătorul uman și o blochează"""
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.grid[row][col] == ' ':  # Căutăm doar celule libere
                    # Verifică dacă punerea unui simbol uman în această celulă ar bloca o victorie
                    self.board.make_move(row, col, self.human_player.token)

                    if self.board.check_victory(self.human_player.token):
                        # Dacă mutarea ar duce la victorie, întoarcem poziția pentru a bloca victoria
                        self.board.grid[row][col] = ' '  # Resetează celula înainte de a face mutarea computerului
                        return (row, col)

                    # Dacă nu găsim o mutare câștigătoare pentru uman, resetăm celula
                    self.board.grid[row][col] = ' '

        return None  # Dacă nu există o mutare câștigătoare de blocat
