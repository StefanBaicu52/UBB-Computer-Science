from src.repository.RentalRepo import RentalRepo
from src.domain.RentalDomain import Rental
import pickle
import random

class RentalBinaryRepo(RentalRepo):
    def __init__(self, file):
        super().__init__()
        self._file = file
        # Load rental data from the file or initialize an empty list if the file does not exist
        self._rental_data = self.load_from_file(self._file)

    def add(self, rental):
        super().add(rental)
        self.save_to_file(self._file)

    def remove(self, rental_id):
        super().remove(rental_id)
        self.save_to_file(self._file)

    def get_next_id(self):
        return super().get_next_id()

    def get_all(self):
        return super().get_all()

    def get_all_books(self):
        return super().get_all_books()

    def get_all_clients(self):
        return super().get_all_clients()

    def find_by_id(self, rental_id):
        return super().find_by_id(rental_id)

    def count_rentals_clients(self, client_id):
        return super().count_rentals_clients(client_id)

    def count_rentals_books(self, book_id):
        return super().count_rentals_books(book_id)

    def update(self, rental):
        super().update(rental)
        self.save_to_file(self._file)

    def save_to_file(self, pickle_file):
        try:
            with open(pickle_file, "wb") as file:
                for rental in self._rental_data:
                    pickle.dump(rental, file)
        except Exception as e:
            print(f"Error saving rentals to file: {e}")

    def list_rentals(self):
        return super().list_rentals()

    def get_last_rental(self):
        return super().get_last_rental()

    def remove_rental(self, rental_id):
        return super().remove_rental(rental_id)

    def add_rentals(self, array):
        return super().add_rentals(array)

    @staticmethod
    def load_from_file(pickle_file):
        temp_data = []
        try:
            with open(pickle_file, "rb") as file:
                while True:
                    try:
                        rental = pickle.load(file)
                        temp_data.append(rental)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found, starting with an empty list.")
        except Exception as e:
            print(f"Error loading rentals from file: {e}")
        return temp_data
