from board import Board, Snakebody
import random

class Controller:
    def __init__(self, n):
        self.board = Board(n)
        self.snake = Snakebody()
        self.size = n
        self.direction = "UP"  #directia initiala
        self.snake_positions = []
        self.apples = []

    def place_snake(self):
        middle = (self.size - 1) // 2
        if middle + 2 >= self.size:
            print("Table is too small for the snake")
            return
        self.board.data[middle][middle] = self.snake.head
        self.board.data[middle + 1][middle] = self.snake.body
        self.board.data[middle + 2][middle] = self.snake.body
        self.snake_positions = [
            (middle, middle),
            (middle + 1, middle),
            (middle + 2, middle)
        ]

    def place_apples(self, num_apples):
        for _ in range(num_apples):
            while True:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                if (row, col) not in self.snake_positions and self.board.data[row][col] == " ":
                    self.board.data[row][col] = "a"
                    self.apples.append((row, col))
                    break

    def move_snake(self, steps=1):
        # Iterăm pentru fiecare pas pe care trebuie să-l facem
        for _ in range(steps):
            head_row, head_col = self.snake_positions[0]

            # Determinăm noua poziție a capului în funcție de direcția curentă
            if self.direction == "UP":
                new_head = (head_row - 1, head_col)
            elif self.direction == "DOWN":
                new_head = (head_row + 1, head_col)
            elif self.direction == "LEFT":
                new_head = (head_row, head_col - 1)
            elif self.direction == "RIGHT":
                new_head = (head_row, head_col + 1)

            # Verificăm dacă ieșim din granițele tablei sau dacă lovim corpul
            if (
                    new_head[0] < 0 or new_head[0] >= self.size or
                    new_head[1] < 0 or new_head[1] >= self.size or
                    new_head in self.snake_positions
            ):
                print("Game Over! Snake hit the wall or itself.")
                exit()

            # Adăugăm capul pe prima poziție
            self.snake_positions.insert(0, new_head)

            # Verificăm dacă am mâncat un măr
            if new_head in self.apples:
                self.apples.remove(new_head)
                self.place_apples(1)  # Plasam un nou mar
            else:
                # Dacă nu am mâncat un măr, eliminăm coada
                tail = self.snake_positions.pop()

                # Ștergem coada de pe tablă
                self.board.data[tail[0]][tail[1]] = " "

            # Actualizăm tabla
            self.board.data[new_head[0]][new_head[1]] = self.snake.head
            for segment in self.snake_positions[1:]:
                self.board.data[segment[0]][segment[1]] = self.snake.body

    def change_direction(self, new_direction):
        # validez schimbarea de directie(nu are voie in oparti opsue sa se miste direct)
        if (
            (self.direction == "UP" and new_direction == "DOWN") or
            (self.direction == "DOWN" and new_direction == "UP") or
            (self.direction == "LEFT" and new_direction == "RIGHT") or
            (self.direction == "RIGHT" and new_direction == "LEFT")
        ):
            print("Invalid move: Cannot reverse direction.")
            return
        self.direction = new_direction