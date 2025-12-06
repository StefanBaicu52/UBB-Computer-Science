from controller import Controller


class UI:
    def __init__(self, settings_file):
        # citirea din fisier
        n, num_apples = self.read_settings_from_file(settings_file)

        # initializez controlerul cu dimenisunea citita
        self.controller = Controller(n)
        self.num_apples = num_apples

    def read_settings_from_file(self, settings_file):
        try:
            with open(settings_file, "r") as f:
                print(f"Fisier {settings_file} gasit!")
                lines = f.readlines()
                if len(lines) < 2:
                    raise ValueError("Fisierul trebuie sa conțina exact doua linii!")
                n = int(lines[0].strip())  # Citim dimensiunea tablei
                num_apples = int(lines[1].strip())  # Citim nr mere
                return n, num_apples
        except FileNotFoundError:
            print(f"Eroare: Fisierul {settings_file} nu a fost gasit!")
            exit()

    def display(self):
        print(self.controller.board)

    def play(self):
        self.controller.place_snake()
        self.controller.place_apples(self.num_apples)
        self.display()

        while True:
            command = input("Alege comanda : move[n] / up / down / left / right / exit : ").strip().lower()
            if command == "exit":
                print("Game Over!")
                break
            elif command.startswith("move"):
                if command=="move":
                    self.controller.move_snake()
                elif command.startswith("move[") and command.endswith("]"):
                    try:
                        steps=int(command[5:-1])
                        self.controller.move_snake(steps)
                    except ValueError:
                        print("Comanda 'move' trebuie urmata de un numar in []")
                else:
                    print("Invalid command!")
            elif command in ["up", "down", "left", "right"]:
                self.controller.change_direction(command.upper())
            else:
                print("Invalid command!")

            self.display()