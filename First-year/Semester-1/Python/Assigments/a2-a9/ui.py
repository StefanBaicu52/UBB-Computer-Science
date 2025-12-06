class ComplexRepositoryError(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + self.__msg


class UI:
    def __init__(self, service):
        self.service = service

    def menu(self):
        print("\nMenu:")
        print("0. Exit")
        print("1. Add complex number")
        print("2. Display all complex numbers")
        print("3. Filter numbers by index range")
        print("4. Undo last operation")

    def start(self):
        while True:
            self.menu()
            choice = input("Your choice: ").strip()

            if choice == "0":
                print("Exiting the program.")
                break
            elif choice == "1":
                self.add_complex_number()
            elif choice == "2":
                self.display_numbers()
            elif choice == "3":
                self.filter_numbers()
            elif choice == "4":
                self.undo()
            else:
                print("Invalid choice. Please try again.")

    def add_complex_number(self):
        try:
            real = int(input("Enter real part: ").strip())
            imaginary = int(input("Enter imaginary part: ").strip())
            self.service.add_complex_number(real, imaginary)
            print("Complex number added successfully.")
        except ValueError:
            print("Invalid input. Please enter integers for real and imaginary parts.")

    def display_numbers(self):
        numbers = self.service.display_numbers()
        if numbers:
            print("List of Complex Numbers:")
            for number in numbers:
                print(number)
        else:
            print("No complex numbers to display.")

    def filter_numbers(self):
        try:
            start = int(input("Enter start index: ").strip())
            end = int(input("Enter end index: ").strip())
            if start < 0 or end < 0 or start > end:
                raise ValueError("Start index must be <= end index, and both must be non-negative.")

            numbers = self.service.filter_numbers(start, end)
            if numbers:
                print("Filtered Complex Numbers:")
                for number in numbers:
                    print(number)
            else:
                print("No complex numbers found in the specified range.")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except IndexError:
            print("Index out of range. Please enter valid indices.")

    def undo(self):
        try:
            self.service.undo()
            print("Last operation undone successfully.")
        except Exception as e:
            print(f"Error: {e}")
