class Board:
    def __init__(self,rows=6,cols=6):
        self.rows = rows
        self.cols = cols
        self.grid=[[' ' for _ in range(self.cols)]for _ in range(self.rows)]

    def valid_move(self,row,col):
        return self.grid[row][col] == ' '

    def make_move(self,row,col,token):
        if self.valid_move(row,col):
            self.grid[row][col]=token
        else:
            raise ValueError("pozitia este deja ocupata")

    def check_victory(self, token):
        # Check horizontal, vertical, and diagonal lines for a win
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row][col + i] == token for i in range(5)):
                    return True
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.grid[row + i][col] == token for i in range(5)):
                    return True
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.grid[row + i][col + i] == token for i in range(5)):
                    return True
                if all(self.grid[row + 3 - i][col + i] == token for i in range(5)):
                    return True
        return False




