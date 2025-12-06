from chaos.board import Board
from chaos.player import Player
import random

class GameController:
    def __init__(self):
        self.board = Board()
        self.human_player=Player("Human","O")
        self.computer_player=Player("Computer","X")
        self.current_player=self.human_player

    def switch_player(self):
        if self.current_player == self.computer_player:
            self.current_player=self.human_player
        else:
            self.current_player=self.computer_player

    def human_move(self,row,column):
        if self.board.valid_move(row,column):
            self.board.make_move(row,column,self.human_player.token)
            if self.board.check_victory(self.human_player.token):
                return "Human wins"
            self.switch_player()
        else:
            raise Exception("Invalid move")
        return "Valid"

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

    def computer_move(self):
        """Permite computerului să facă o mutare aleatorie sau să blocheze victoria umanului"""
        # Încearcă să blocheze victoria umanului
        block_move = self.block_human_win()

        if block_move:
            # Dacă există o mutare de blocat, computerul o face
            row, col = block_move
            self.board.make_move(row, col, self.computer_player.token)
            self.switch_player()
            print(f"Computerul a blocat victoria umanului la ({row}, {col})")
        else:
            # Dacă nu există o mutare de blocat, alege aleatoriu o mutare validă
            empty_cells = [(r, c) for r in range(self.board.rows) for c in range(self.board.cols) if
                           self.board.valid_move(r, c)]
            if empty_cells:
                row, col = random.choice(empty_cells)
                self.board.make_move(row, col, self.computer_player.token)
                if self.board.check_victory(self.computer_player.token):
                    return "Computer wins"
                self.switch_player()
            else:
                return "Computer wins"







