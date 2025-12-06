from classes import Complex
import random


class MemRepo:
    def __init__(self):
        # Initialize _data and _history
        self._data = []
        self._history = []

        # Populate the repository with random complex numbers
        for _ in range(10):  # Generate 10 random complex numbers
            real_part = random.randint(1, 10)
            imag_part = random.randint(1, 10)
            complex_number = Complex(real_part, imag_part)
            self._data.append(complex_number)

        # Save the initial state in the history list
        self._history.append(self._data[:])  # Shallow copy is sufficient here

    def add(self, new_number: Complex):
        """
        Adds a number to the repository.
        :param new_number: Complex object
        """
        self._data.append(new_number)
        self._history.append(self._data[:])  # Save current state to history

    def remove(self, start_idx, end_idx):
        """
        Removes complex numbers from the repository based on index range.
        :param start_idx: Start index (inclusive)
        :param end_idx: End index (inclusive)
        """
        if start_idx < 0 or end_idx >= len(self._data) or start_idx > end_idx:
            raise IndexError("Invalid index range.")

        del self._data[start_idx:end_idx + 1]  # Remove the elements directly
        self._history.append(self._data[:])  # Save current state to history

    def get_all(self):
        """
        Returns the list of all complex numbers.
        :return: List of Complex objects
        """
        return self._data

    def get_history(self):
        """
        Returns the history of repository states.
        :return: List[List[Complex]]
        """
        return self._history

    def undo(self):
        """
        Undoes the last operation (either add or remove).
        """
        if len(self._history) > 1:
            self._history.pop()  # Remove the current state from history
            self._data = self._history[-1][:]  # Restore the previous state
        else:
            print("No operations to undo.")
