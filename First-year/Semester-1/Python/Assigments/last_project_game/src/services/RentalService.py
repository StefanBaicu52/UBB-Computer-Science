
from src.domain.RentalDomain import Rental
from datetime import datetime, date


class RentalService:
    def __init__(self, rental_repository):
        """
        Constructor for RentalService class
        :param rental_repository:
        """
        self.__rental_repository = rental_repository

    def rent_book(self, client_id, book_id):
        """
        Rents a book
        :param client_id:
        :param book_id:
        :return:
        """
        today = date.today()
        rental_id = self.__rental_repository.get_next_id()

        rental = Rental(str(rental_id), str(client_id), str(book_id), today,"0")
        self.__rental_repository.add(rental)

    def add_rental(self, rental):
        self.__rental_repository.add(rental)

    def check_rental_id(self, rental_id):
        """
        Checks if a rental ID exists
        :param rental_id:
        :return:
        """
        for rental in self.__rental_repository.get_all():
            if rental.rental_id() == rental_id:
                return True
        return False

    def check_returned_date(self, rental_id):
        """
        Checks if a book has been returned
        :param rental_id:
        :return:
        """
        for rental in self.__rental_repository.get_all():
            if rental.rental_id() == rental_id:
                if rental.returned_date() == "0":
                    return True
        return False

    def return_book(self, rental_id):
        """
        Returns a book
        :param rental_id:
        :return:
        """
        rental = self.__rental_repository.find_by_id(rental_id)
        rental.set_returned_date(date.today())
        self.__rental_repository.update(rental)

    def remove_rental(self, rental_id):
        """
        Removes a rental
        :param rental_id:
        :return:
        """
        self.__rental_repository.remove(rental_id)


    def most_rented_books(self):
        """
        Returns a list of most rented books
        :return:
        """
        rented_books = []

        for rental in self.__rental_repository.get_all_books():
            count = self.__rental_repository.count_rentals_books(rental)
            if (rental, count) not in rented_books:
                rented_books.append((rental, count))

        rented_books.sort(key=lambda x: x[1], reverse=True)

        return rented_books

    def most_active_clients(self):
        """
        Returns a list of most active clients
        :return:
        """
        active_clients = []

        for rental in self.__rental_repository.get_all_clients():
            count = self.__rental_repository.count_rentals_clients(rental)
            if (rental, count) not in active_clients:
                active_clients.append((rental, count))

        active_clients.sort(key=lambda x: x[1], reverse=True)

        return active_clients

    def get_last_rental(self):
        """
        Returns the last rental
        :return:
        """
        return self.__rental_repository.get_last_rental()

    def rental_id(self):
        """
        Returns the rental ID
        :return:
        """
        return self.__rental_repository.get_next_id()

    def book_id(self):
        """
        Returns the book ID
        :return:
        """
        return self.__rental_repository.get_all_movies()

    def client_id(self):
        """
        Returns the client ID
        :return:
        """
        return self.__rental_repository.get_all_clients()

    def rented_date(self):
        """
        Returns the rented date
        :return:
        """
        return self.__rental_repository.get_rented_date()


    def returned_date(self):
        """
        Returns the returned date
        :return:
        """
        return self.__rental_repository.get_returned_date()

    def get_rental(self, rental_id):
        return self.__rental_repository.find_by_id(rental_id)

    def add_rentals(self, array):
        self.__rental_repository.add_rentals(array)
