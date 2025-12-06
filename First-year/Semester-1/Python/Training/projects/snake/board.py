from texttable import Texttable
class Board:
    def __init__(self,n):
        self.n = n
        self.data = [[" " for _ in range(n)] for _ in range(n)]


    def __str__(self):
        self.table = Texttable()
        self.table.add_rows(self.data, [])
        return self.table.draw()

class Snakebody:
    def __init__(self):
        self.head='*'
        self.body='+'
