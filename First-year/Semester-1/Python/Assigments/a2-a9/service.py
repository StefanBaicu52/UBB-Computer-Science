from classes import Complex
from memory_repository import MemRepo

class Services:
    def __init__(self, repository):
        self.__repo = repository

    def add_complex_number(self, real, imaginary):
        """
        Create a Complex number and add it to the repository.
        """
        new_number = Complex(real, imaginary)
        self.__repo.add(new_number)

    def display_numbers(self):
        """
        Return all complex numbers in the repository.
        """
        return self.__repo.get_all()

    def filter_numbers(self, start, end):
        """
        Filter the numbers between start and end indices.
        """
        numbers = self.__repo.get_all()
        # Validate indices
        if start < 0 or end >= len(numbers) or start > end:
            raise IndexError("Invalid start or end index.")
        return numbers[start:end + 1]

    def undo(self):
        """
        Undo the last operation.
        """
        self.__repo.undo()
