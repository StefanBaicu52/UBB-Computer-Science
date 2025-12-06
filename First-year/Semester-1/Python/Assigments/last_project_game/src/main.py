from ui.ui import UI
import configparser

from services.ClientService import ClientService
from services.BookService import BookService
from services.RentalService import RentalService
from services.UndoService import UndoService

from repository.ClientRepo import ClientRepo
from repository.BookRepo import BookRepo
from repository.RentalRepo import RentalRepo
from repository.ClientTextRepo import ClientTextRepo
from repository.BookTextRepo import BookTextRepo
from repository.RentalTextRepo import RentalTextRepo
from repository.ClientBinaryRepo import ClientBinaryRepo
from repository.BookBinaryRepo import BookBinaryRepo
from repository.RentalBinaryRepo import RentalBinaryRepo

from datetime import date as day
import unittest

from src.test.test import TestClientService
from src.test.test import TestBookService
from src.test.test import TestRentalService


def start():
    print("Today is", day.today(), "\n")
    while True:
        UI.input()


def for_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClientService)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBookService))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRentalService))
    unittest.TextTestRunner().run(suite)


def config_settings():
    config = configparser.ConfigParser()
    config.read('settings.properties')
    client_repos = None
    book_repos = None
    rental_repos = None

    repository_name = config.get('Config', 'repository')

    if repository_name == "binary":
        client_repo_file_name = config.get('Config', 'client_repo_file')
        book_repo_file_name = config.get('Config', 'book_repo_file')
        rental_repo_file_name = config.get('Config', 'rental_repo_file')

        rental_repos = RentalBinaryRepo(rental_repo_file_name)
        client_repos = ClientBinaryRepo(client_repo_file_name, rental_repos)
        book_repos = BookBinaryRepo(book_repo_file_name, rental_repos)

        repository_name = "Binary"
    elif repository_name == "text":
        client_repo_file_name = config.get('Config', 'client_repo_file')
        book_repo_file_name = config.get('Config', 'book_repo_file')
        rental_repo_file_name = config.get('Config', 'rental_repo_file')

        rental_repos = RentalTextRepo(rental_repo_file_name)
        client_repos = ClientTextRepo(client_repo_file_name, rental_repos)
        book_repos = BookTextRepo(book_repo_file_name, rental_repos)

        repository_name = "Text"
    elif repository_name == "memory":
        rental_repos = RentalRepo()
        client_repos = ClientRepo(rental_repos)
        book_repos = BookRepo(rental_repos)

        repository_name = "Memory"

    print(f"Using repository: {repository_name}\n")

    return client_repos, book_repos, rental_repos


if __name__ == '__main__':
    for_tests()
    Client_Repo, Book_Repo, Rental_Repo = config_settings()

    Client_Service = ClientService(Client_Repo)
    Book_Service = BookService(Book_Repo)
    Rental_Service = RentalService(Rental_Repo)

    UndoService = UndoService(Client_Service, Book_Service, Rental_Service)

    UI = UI(Client_Service, Book_Service, Rental_Service, UndoService)

    start()