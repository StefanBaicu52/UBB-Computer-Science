import unittest
from classes import *
from memory_repository import *
from service import *


class TestComplex(unittest.TestCase):
    def test_complex_initialization(self):
        c = Complex(2, 3)
        self.assertEqual(c.real, 2)
        self.assertEqual(c.imaginary, 3)
        self.assertEqual(str(c), "2 + 3i")


class TestMemRepo(unittest.TestCase):
    def setUp(self):
        self.repo = MemRepo()

    def test_add(self):
        new_complex = Complex(5, 6)
        self.repo.add(new_complex)
        self.assertIn(new_complex, self.repo.get_all())

    def test_remove(self):
        initial_length = len(self.repo.get_all())
        self.repo.remove(0, 1)
        self.assertEqual(len(self.repo.get_all()), initial_length - 2)

    def test_invalid_remove(self):
        with self.assertRaises(IndexError):
            self.repo.remove(-1, 100)  # Invalid range

    def test_undo(self):
        original_data = self.repo.get_all()[:]
        self.repo.add(Complex(7, 8))
        self.repo.undo()
        self.assertEqual(self.repo.get_all(), original_data)

    def test_no_undo_available(self):
        self.repo.undo()
        self.repo.undo()  # Undo should only work once here
        self.repo.undo()
        self.assertEqual(len(self.repo.get_all()), 10)


class TestServices(unittest.TestCase):
    def setUp(self):
        self.repo = MemRepo()
        self.service = Services(self.repo)

    def test_add_complex_number(self):
        self.service.add_complex_number(4, 5)
        self.assertEqual(str(self.repo.get_all()[-1]), "4 + 5i")

    def test_display_numbers(self):
        numbers = self.service.display_numbers()
        self.assertEqual(numbers, self.repo.get_all())

    def test_filter_numbers(self):
        all_numbers = self.repo.get_all()
        filtered = self.service.filter_numbers(0, 2)
        self.assertEqual(filtered, all_numbers[0:3])

    def test_filter_invalid_range(self):
        with self.assertRaises(IndexError):
            self.service.filter_numbers(5, 2)  # Start index is greater than end index

    def test_undo(self):
        self.service.add_complex_number(4, 5)
        self.service.undo()
        self.assertEqual(len(self.repo.get_all()), 10)  # Undo reverts to original length


