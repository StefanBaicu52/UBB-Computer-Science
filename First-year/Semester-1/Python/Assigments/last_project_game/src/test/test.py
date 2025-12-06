
import unittest
from src.services.ClientService import ClientService
from src.services.BookService import BookService
from src.repository.ClientRepo import ClientRepo
from src.repository.BookRepo import BookRepo
from src.repository.RentalRepo import RentalRepo
from src.services.RentalService import RentalService
from src.domain.RentalDomain import Rental
from src.domain.ClientDomain import Client
from src.domain.BookDomain import Book


class TestClientService(unittest.TestCase):
    def setUp(self):
        self.__client_repository = ClientRepo(RentalRepo())
        self.__client_service = ClientService(self.__client_repository)

    def test_client_add(self):
        self.__client_service.add_client(1, "Client1")
        self.assertEqual(len(self.__client_repository.list_clients()), 21)

    def test_client_update(self):
        self.__client_service.update_client("3", "Client1")
        self.assertEqual(self.__client_service.can_update_client("3"), True)
        self.assertEqual(self.__client_repository.list_clients()[2].client_name(), "Client1")

    def test_client_uniques(self):
        self.assertEqual(self.__client_service.check_client_id_unique("1"), False)
        self.assertEqual(self.__client_service.check_client_id_unique("21"), True)
        self.assertEqual(self.__client_service.check_client_id("1"), True)

    def test_client_remove(self):
        self.assertEqual(self.__client_service.can_remove_client("2"), True)
        self.assertEqual(self.__client_service.can_remove_client("21"), False)
        self.__client_service.remove_client("2")
        self.assertEqual(len(self.__client_repository.list_clients()), 19)
        self.assertEqual(self.__client_service.can_remove_client("2"), False)

    def tests_for_domain(self):
        self.assertEqual(self.__client_repository.list_clients()[0].client_id(), "1")
        self.assertEqual(self.__client_repository.list_clients()[0].client_name(), "Client1")
        self.assertEqual(str(self.__client_repository.list_clients()[0]), "#1 Client1")
        self.assertEqual(self.__client_repository.list_clients()[0].client_id(), "1")
        self.assertEqual(self.__client_repository.list_clients()[0].client_name(), "Client1")
        self.assertEqual(str(self.__client_repository.list_clients()[0]), "#1 Client1")
        self.__client_service.search_client_by_name("Client1")
        self.__client_service.search_client_by_id("1")


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.__book_repository = BookRepo(RentalRepo())
        self.__book_service = BookService(self.__book_repository)

    def test_book_add(self):
        self.__book_service.add_book(21, "book21", "Author21")
        self.assertEqual(len(self.__book_repository.get_all_books()), 21)

    def test_book_update(self):
        self.__book_service.update_book("3", "book1", "Author1")
        self.assertEqual(self.__book_service.can_update_book("3"), True)
        self.assertEqual(self.__book_repository.get_all_books()[2].book_title(), "book1")
        self.assertEqual(self.__book_repository.get_all_books()[2].book_author(), "Author1")

    def test_book_uniques(self):
        self.assertEqual(self.__book_service.check_book_id_unique("1"), False)
        self.assertEqual(self.__book_service.check_book_id("1"), True)

    def test_book_remove(self):
        self.assertEqual(self.__book_service.can_remove_book("2"), True)
        self.assertEqual(self.__book_service.can_remove_book("21"), False)
        self.__book_service.remove_book("2")
        self.assertEqual(len(self.__book_repository.get_all_books()), 19)
        self.assertEqual(self.__book_service.can_remove_book("2"), False)
        self.__book_service.search_book_by_id("1")
        self.__book_service.search_book_by_title("book1")
        self.__book_service.search_book_by_author("Author1")
        self.__book_service.list_books()
        self.__book_service.check_book_id_unique("1")


class TestRentalService(unittest.TestCase):
    def setUp(self):
        self.__book_repository = BookRepo(RentalRepo())
        self.__client_repository = ClientRepo(RentalRepo())
        self.__rental_repository = RentalRepo()
        self.__rental_service = RentalService(self.__rental_repository)


    def test_rental_service(self):
        self.__rental_repository.get_all_clients()
        self.__rental_repository.get_all_books()
        self.__rental_repository.find_by_id("1")
        self.__rental_repository.count_rentals_books("1")
        self.__rental_repository.count_rentals_clients("1")
        self.__rental_repository.update(Rental("1", "1", "1", "1",  "1"))

        self.__rental_service.rent_book("1", "1")
        self.__rental_service.check_rental_id("1")
        self.__rental_service.check_returned_date("1")
        self.__rental_service.return_book("1")
        self.__rental_service.most_rented_books()
        self.__rental_service.most_active_clients()



if __name__ == '__main__':
    unittest.main()
