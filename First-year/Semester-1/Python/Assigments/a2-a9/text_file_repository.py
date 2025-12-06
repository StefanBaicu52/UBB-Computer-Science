from classes import Complex
from memory_repository import MemRepo

class TextRepo(MemRepo):
    def __init__(self):
        """
        Constructor for the text repository.
        """
        super().__init__()
        self._data = self.load_from_file("textfile.txt")
        self._history = []  # Using a list to track repository states
        if len(self._data) > 0:
            self._history.append(self._data.copy())
        else:
            self._history.append([])

    def add(self, new_number: Complex):
        """
        Adds a complex number to the repository.
        :param new_number: Complex
        :return: None
        """
        super().add(new_number)
        self._history.append(self._data.copy())
        self.save_to_file("textfile.txt")

    def remove(self, start, end):
        """
        Removes complex numbers from the repository based on index range.
        :param start: Start index
        :param end: End index
        :return: None
        """
        super().remove(start, end)
        self._history.append(self._data.copy())
        self.save_to_file("textfile.txt")

    def undo(self):
        """
        Undoes the last operation (either add or remove).
        :return: None
        """
        if len(self._history) > 1:
            # Revert to the previous state
            self._history.pop()  # Remove the most recent state
            self._data = self._history[-1].copy()  # Revert to the last saved state
            self.save_to_file("textfile.txt")
        else:
            print("No operations to undo.")

    def load_from_file(self, textfile):
        """
        Loads the list from a text file.
        :param textfile: File name
        :return: List[Complex]
        """
        try:
            temp_data = []
            with open(textfile, "r") as file:
                for line in file:
                    line = line.strip()  # Remove any leading/trailing whitespace
                    if line:
                        real, imaginary = map(int, line.split(","))
                        temp_data.append(Complex(real, imaginary))  # Create Complex number
            return temp_data
        except IOError:
            print("Error: Unable to load file.")
            return []

    def save_to_file(self, textfile):
        """
        Saves the list to a text file.
        :param textfile: File name
        :return: None
        """
        try:
            with open(textfile, "w") as file:
                for complex_number in self._data:
                    file.write(f"{complex_number.real},{complex_number.imaginary}\n")
        except IOError as e:
            print("Error:", e)
