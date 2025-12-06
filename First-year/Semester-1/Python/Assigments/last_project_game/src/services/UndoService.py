
from src.domain.ClientDomain import Client
from src.domain.BookDomain import Book
from src.domain.RentalDomain import Rental
from src.exceptions.Exceptions import UndoRedoException


class UndoService:
    def __init__(self, client_service, book_service, rental_service):
        self._redo_operations = []
        self._undo_operations = []
        self._index = -1

        self._client_service = client_service
        self._book_service = book_service
        self._rental_service = rental_service

    def client_adding_operation(self, client_id, client_name):
        client = Client(client_id, client_name)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["client", "add", client])
        self._undo_operations.append(["client", "remove", client_id])
        self._index += 1

    def client_removing_operation(self, client_id, client_name, array):
        client = Client(client_id, client_name)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["client", "remove", client_id])
        self._undo_operations.append(["client", "add", client, array])
        self._index += 1

    def client_updating_operation(self, client_id, client_name, old_client_name):
        client = Client(client_id, client_name)
        old_client = Client(client_id, old_client_name)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["client", "update", client])
        self._undo_operations.append(["client", "update", old_client])
        self._index += 1

    def book_adding_operation(self, book_id, book_title, book_author):
        book = Book(book_id, book_title, book_author)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["book", "add", book])
        self._undo_operations.append(["book", "remove", book_id])
        self._index += 1

    def book_removing_operation(self, book_id, book_title, book_author, array):
        book = Book(book_id, book_title, book_author)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["book", "remove", book_id])
        self._undo_operations.append(["book", "add", book, array])
        self._index += 1

    def book_updating_operation(self, book_id, book_title, book_author,
                                 old_book_title, old_book_author):
        book = Book(book_id, book_title, book_author)
        old_book = Book(book_id, old_book_title, old_book_author)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["book", "update", book])
        self._undo_operations.append(["book", "update", old_book])
        self._index += 1

    def rental_adding_operation(self, rental_id, book_id, client_id, rented_date, returned_date):
        rental = Rental(rental_id, book_id, client_id, rented_date, returned_date)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["rental", "add", rental])
        self._undo_operations.append(["rental", "remove", rental_id])
        self._index += 1

    def rental_removing_operation(self, rental_id, book_id, client_id,
                                  rented_date, returned_date):
        rental = Rental(rental_id, book_id, client_id, rented_date, returned_date)

        self._redo_operations = self._redo_operations[:self._index + 1]
        self._undo_operations = self._undo_operations[:self._index + 1]

        self._redo_operations.append(["rental", "remove", rental_id])
        self._undo_operations.append(["rental", "add", rental])
        self._index += 1

    def redo(self):
        if self._index == len(self._redo_operations) - 1:
            raise UndoRedoException("No more operations to redo!\n")

        self._index += 1

        operation = self._redo_operations[self._index]
        if operation[0] == "client":
            if operation[1] == "add":
                self._client_service.add_client(operation[2].client_id(), operation[2].client_name())
            elif operation[1] == "remove":
                self._client_service.remove_client(operation[2])
            elif operation[1] == "update":
                self._client_service.update_client(operation[2].client_id(), operation[2].client_name())
        elif operation[0] == "book":
            if operation[1] == "add":
                self._book_service.add_book(operation[2].book_id(), operation[2].book_title(),
                                              operation[2].book_author())
            elif operation[1] == "remove":
                self._book_service.remove_book(operation[2])
            elif operation[1] == "update":
                self._book_service.update_book(operation[2].book_id(), operation[2].book_title(),
                                                 operation[2].book_author())
        elif operation[0] == "rental":
            if operation[1] == "add":
                rental = [Rental(operation[2].rental_id(), operation[2].book_id(), operation[2].client_id(),
                                 operation[2].rented_date(), operation[2].returned_date())]
                self._rental_service.add_rentals(rental)
            elif operation[1] == "remove":
                self._rental_service.remove_rental(operation[2])

    def undo(self):
        if self._index == -1:
            raise UndoRedoException("No more operations to undo!\n")
        operation = self._undo_operations[self._index]
        if operation[0] == "client":
            if operation[1] == "add":
                self._client_service.add_client(operation[2].client_id(), operation[2].client_name())
                self._rental_service.add_rentals(operation[3])
            elif operation[1] == "remove":
                test = operation[2]
                self._client_service.remove_client(operation[2])
            elif operation[1] == "update":
                self._client_service.update_client(operation[2].client_id(), operation[2].client_name())
        elif operation[0] == "book":
            if operation[1] == "add":
                self._book_service.add_book(operation[2].book_id(), operation[2].book_title(),
                                              operation[2].book_author())
                self._rental_service.add_rentals(operation[3])
            elif operation[1] == "remove":
                self._book_service.remove_book(operation[2])
            elif operation[1] == "update":
                self._book_service.update_book(operation[2].book_id(), operation[2].book_title(),
                                                 operation[2].book_author())
        elif operation[0] == "rental":
            if operation[1] == "add":
                rental = [Rental(operation[2].rental_id(), operation[2].book_id(), operation[2].client_id(),
                                 operation[2].rented_date(), operation[2].returned_date())]
                self._rental_service.add_rentals(rental)
            elif operation[1] == "remove":
                self._rental_service.remove_rental(operation[2])

        self._index -= 1
