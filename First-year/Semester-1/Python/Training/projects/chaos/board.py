class Board:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def valid_move(self, row, col, placement_phase=True):
        return self.grid[row][col] == ' '  # ✅ Mutarea este validă doar dacă celula este goală!

    def make_move(self, row, col, token):
        if self.valid_move(row, col, placement_phase=True):
            self.grid[row][col] = token
        else:
            raise ValueError("Invalid move. Position is occupied.")

    def move_piece(self, from_row, from_col, to_row, to_col):
        if self.grid[from_row][from_col] == ' ':
            raise ValueError("No piece at selected position.")
        if not self.valid_move(to_row, to_col, placement_phase=False):
            raise ValueError("Invalid move. Target position is occupied.")

        # ✅ Mutarea este permisă oriunde (fără restricția de adiacență)
        self.grid[to_row][to_col] = self.grid[from_row][from_col]
        self.grid[from_row][from_col] = ' '

    def check_victory(self, token):
        # Verifică linii
        for row in range(self.rows):
            if all(self.grid[row][col] == token for col in range(self.cols)):
                return True

        # Verifică coloane
        for col in range(self.cols):
            if all(self.grid[row][col] == token for row in range(self.rows)):
                return True

        # Verifică diagonala principală
        if all(self.grid[i][i] == token for i in range(self.rows)):
            return True

        # Verifică diagonala secundară
        if all(self.grid[i][self.cols - 1 - i] == token for i in range(self.rows)):
            return True

        return False
