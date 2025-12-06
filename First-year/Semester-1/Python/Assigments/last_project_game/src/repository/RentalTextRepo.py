from src.repository.RentalRepo import RentalRepo
from src.domain.RentalDomain import Rental

class RentalTextRepo(RentalRepo):
    def __init__(self, file):
        super().__init__()
        self._file = file
        # Load rental data from the file or initialize with an empty list if file is not found
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

    def list_rentals(self):
        return super().list_rentals()

    def get_last_rental(self):
        return super().get_last_rental()

    def remove_rental(self, rental_id):
        return super().remove_rental(rental_id)

    def add_rentals(self, array):
        return super().add_rentals(array)

    def save_to_file(self, textfile):
        try:
            with open(textfile, "w") as file:
                for rental in self._rental_data:
                    file.write(f"{rental.rental_id()},{rental.book_id()},{rental.client_id()},"
                               f"{rental.rented_date()},{rental.returned_date()}\n")
        except Exception as e:
            print(f"Error saving rentals to file: {e}")

    def load_from_file(self, textfile):
        temp_data = []
        try:
            with open(textfile, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip().split(",")
                    rental = Rental(line[0], line[1], line[2], line[3], line[4])
                    temp_data.append(rental)
        except FileNotFoundError:
            print("File not found, starting with an empty list.")
        except Exception as e:
            print(f"Error loading rentals from file: {e}")
        return temp_data
