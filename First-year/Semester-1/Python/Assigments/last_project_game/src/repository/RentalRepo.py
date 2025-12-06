from src.domain.RentalDomain import Rental
from datetime import date, timedelta
import random


class RentalRepo:
    def __init__(self):
        """
        Creates a new instance of RentalRepo
        """
        self.__rental_data = []
        today = date.today()

        for counter in range(1, 21):
            days_in_future = random.randint(-365, 365)
            future_date = today + timedelta(days=days_in_future)
            self.__rental_data.append(Rental(str(counter), str(counter),
                                             str(random.randint(1, 20)), today, future_date))

    def add(self, rental):
        """
        Adds a new rental to the repository
        :param rental:
        :return:
        """
        self.__rental_data.append(rental)

    def remove(self, rental_id):
        """
        Removes a rental from the repository
        :param rental_id:
        :return:
        """
        for rental in self.__rental_data:
            if rental.rental_id() == rental_id:
                self.__rental_data.remove(rental)

    def get_next_id(self):
        """
        Returns the next id for a rental
        :return:
        """
        return len(self.__rental_data) + 1

    def get_all(self):
        """
        Returns all the rentals
        :return:
        """
        return self.__rental_data

    def get_all_books(self):
        """
        Returns all the books
        :return:
        """
        books = []
        for rental in self.__rental_data:
            books.append(rental.book_id())
        return books

    def get_all_clients(self):
        """
        Returns all the clients
        :return:
        """
        clients = []
        for rental in self.__rental_data:
            clients.append(rental.client_id())
        return clients

    def find_by_id(self, rental_id):
        """
        Finds a rental by id
        :param rental_id:
        :return:
        """
        for rental in self.__rental_data:
            if rental.rental_id() == rental_id:
                return rental

    def count_rentals_books(self, book_id):
        """
        Counts the number of rentals for a book
        :param book_id:
        :return:
        """
        counter = 0
        for rental in self.__rental_data:
            if rental.book_id() == book_id:
                counter += 1
        return counter

    def count_rentals_clients(self, client_id):
        """
        Counts the number of rentals for a client
        :param client_id:
        :return:
        """
        counter = 0
        for rental in self.__rental_data:
            if rental.client_id() == client_id:
                counter += 1
        return counter

    def update(self, rental):
        """
        Updates a rental
        :param rental:
        :return:
        """
        for index in range(len(self.__rental_data)):
            if self.__rental_data[index].rental_id() == rental.rental_id():
                self.__rental_data[index] = rental
                break

    def list_rentals(self):
        """
        Returns the list of rentals
        :return:
        """
        return self.__rental_data

    def get_last_rental(self):
        """
        Returns the last rental
        :return:
        """
        return self.__rental_data[-1]

    def remove_rental(self, rental_id):
        """
        Removes a rental
        :param rental_id:
        :return:
        """
        for rental in self.__rental_data:
            if rental.rental_id() == rental_id:
                self.__rental_data.remove(rental)

    def add_rentals(self, array):
        """
        Adds multiple rentals to the repository
        :param array:
        :return:
        """
        for rental in array:
            self.__rental_data.append(rental)
