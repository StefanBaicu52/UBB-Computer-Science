import pickle
from classes import Complex
from memory_repository import MemRepo
import random


class BinaryRepo(MemRepo):
    def __init__(self):
        """
        Constructor for the binary repository
        """
        super().__init__()

        # Try to load data from the binary file
        self._data = self.load_from_file("binary.pkl")

        # If the binary file is empty or does not exist, generate 10 random numbers
        if not self._data:
            self._data = self.generate_random_complex_numbers(10)
            self.save_to_file("binary.pkl")  # Save the generated numbers to the file

        # Initialize the history list to store all repository states
        self._history = [self._data.copy()]

    def add(self, new_number: Complex):
        """
        Adds a number to the repository
        :param new_number: Complex
        :return: None
        """
        super().add(new_number)
        self._history.append(self._data.copy())
        self.save_to_file("binary.pkl")

    def remove(self, start, end):
        """
        Removes a number from the repository
        :param start: Start index
        :param end: End index
        :return: None
        """
        super().remove(start, end)
        self._history.append(self._data.copy())
        self.save_to_file("binary.pkl")

    def undo(self):
        """
        Undoes the last operation
        :return: None
        """
        if len(self._history) > 1:
            # Revert to the previous state
            self._history.pop()  # Remove the current state
            self._data = self._history[-1].copy()  # Revert to the last saved state
            self.save_to_file("binary.pkl")
        else:
            print("No operations to undo.")

    @staticmethod
    def load_from_file(pkl_file):
        """
        Loads the list from a binary file
        :param pkl_file: File name
        :return: List of numbers
        """
        try:
            with open(pkl_file, "rb") as file:
                temp_data = []
                while True:
                    try:
                        student = pickle.load(file)
                        temp_data.append(student)
                    except EOFError:
                        break
            return temp_data
        except FileNotFoundError:
            return None

    def save_to_file(self, pkl_file):
        """
        Saves the list to a binary file
        :param pkl_file: File name
        :return: None
        """
        with open(pkl_file, "wb") as file:
            for student in self._data:
                pickle.dump(student, file)

    @staticmethod
    def generate_random_complex_numbers(count):
        """
        Generates a list of random Complex numbers
        :param count: Number of complex numbers to generate
        :return: List of Complex objects
        """
        random_numbers = []
        for _ in range(count):
            real_part = random.randint(1, 10)  # Random real part between 1 and 10
            imag_part = random.randint(1, 10)  # Random imaginary part between 1 and 10
            complex_number = Complex(real_part, imag_part)
            random_numbers.append(complex_number)
        return random_numbers
