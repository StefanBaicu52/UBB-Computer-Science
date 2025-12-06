class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]

    def is_valid_move(self, column):
        return self.grid[0][column] == ' '

    def make_move(self, column, token):
        for row in reversed(range(self.rows)):
            if self.grid[row][column] == ' ':
                self.grid[row][column] = token
                return row, column
        return None

    def check_victory(self, token):
        # Check horizontal, vertical, and diagonal lines for a win
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row][col + i] == token for i in range(4)):
                    return True
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if all(self.grid[row + i][col] == token for i in range(4)):
                    return True
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i][col + i] == token for i in range(4)):
                    return True
                if all(self.grid[row + 3 - i][col + i] == token for i in range(4)):
                    return True
        return False
