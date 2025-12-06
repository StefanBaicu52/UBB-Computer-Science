
from src.exceptions.Exceptions import ValidationException
from src.exceptions.Exceptions import RepositoryException
from src.exceptions.Exceptions import UndoRedoException


class UI:
    def __init__(self, client_service, book_service, rental_service, undo_service):
        """
        Initializes the UI class.
        :param client_service:
        :param book_service:
        :param rental_service:
        """
        self.__client_service = client_service
        self.__book_service = book_service
        self.__rental_service = rental_service
        self.__undo_service = undo_service

    def input(self):
        """
        Reads the input from the user.
        :return:
        """
        while True:
            print("Hello! Welcome to the book rental store!\n"
                  "Please choose one of the following options:\n"
                  "[1] Manage clients or books (add/remove/update/list)\n"
                  "[2] Rent or return a book\n"
                  "[3] Search (clients/books)\n"
                  "[4] Statistics\n"
                  "[5] Undo/Redo\n"
                  "[0] Exit\n")
            try:
                command = input("Enter command: ").strip()
                if command == '0':
                    print("Thank you for using our services!")
                    quit()
                elif command == '1':
                    self.manage()
                elif command == '2':
                    self.rent_or_return_book()
                elif command == '3':
                    self.search()
                elif command == '4':
                    self.statistics()
                elif command == '5':
                    self.undo_menu()
                else:
                    raise ValidationException("Invalid command!\n")
            except ValidationException as ve:
                print(ve)

    # 1
    def manage(self):
        """
        Menu for the first option.
        :return:
        """
        while True:
            print("What would you like to manage?\n"
                  "[1] Clients\n"
                  "[2] books\n"
                  "[3] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.manage_clients()
                elif command == '2':
                    self.manage_books()
                elif command == '3':
                    break
                else:
                    raise ValidationException("Invalid command!\n")
            except ValidationException as ve:
                print(ve)

    # 1.1
    def manage_clients(self):
        """
        Menu for managing clients.
        :return:
        """
        while True:
            print("What would you like to do?\n"
                  "[1] Add a client\n"
                  "[2] Remove a client\n"
                  "[3] Update a client\n"
                  "[4] List clients\n"
                  "[5] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.add_client()
                elif command == '2':
                    self.remove_client()
                elif command == '3':
                    self.update_client()
                elif command == '4':
                    self.list_clients()
                elif command == '5':
                    break
                else:
                    raise ValidationException("Invalid command!\n")
            except ValidationException as ve:
                print(ve)

    # 1.1.1
    def add_client(self):
        """
        UI part of adding a client.
        :return:
        """
        try:
            print("Please enter the following information using syntax:\n"
                  "<ID> <Name>\n")
            syntax = input("Enter information: ")
            syntax = syntax.split(" ")
            if len(syntax) == 2:
                if syntax[0].isdigit():
                    if syntax[1].isalpha():
                        if self.__client_service.check_client_id_unique(syntax[0]):
                            self.__client_service.add_client(syntax[0], syntax[1])
                            self.__undo_service.client_adding_operation(syntax[0], syntax[1])
                        else:
                            raise RepositoryException("\nError: Client ID already exists!\n")
                    else:
                        raise ValidationException("\nError: Name is not valid!\n")
                else:
                    raise ValidationException("\nError: ID has to be a positive integer!\n")
            else:
                raise ValidationException("\nError: Invalid syntax!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("Client added successfully!\n")

    # 1.1.2
    def remove_client(self):
        """
        UI part of removing a client.
        :return:
        """
        try:
            print("Please enter the ID of the client you want to remove.\n")
            client_id = input("Enter ID: ").strip()
            if client_id.isdigit():
                if self.__client_service.can_remove_client(client_id):
                    test = self.__client_service.get_client_name(client_id)
                    array = self.__client_service.remove_client(client_id)
                    if array is not None:
                        self.__undo_service.client_removing_operation(client_id,
                                                                      test,
                                                                      array)
                else:
                    raise RepositoryException("\nError: No client has the requested ID!\n")
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("Client removed successfully!\n")

    # 1.1.3
    def update_client(self):
        """
        UI part of updating a client.
        :return:
        """
        try:
            print("Please enter the ID of the client you wish to update.\n")
            client_id = input("Enter ID: ").strip()
            if client_id.isdigit():
                if self.__client_service.can_update_client(client_id):
                    print("Please update the name of the client that has the requested ID.\n")
                    client_name = input("Enter name: ").strip()
                    if client_name.isalpha():
                        self.__undo_service.client_updating_operation(client_id, client_name,
                                                                      self.__client_service.get_client_name(client_id))
                        self.__client_service.update_client(client_id, client_name)
                    else:
                        raise ValidationException("\nError: Name is not valid!\n")
                else:
                    raise RepositoryException("\nError: No client has the requested ID!\n")
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("Client updated successfully!\n")

    # 1.1.4
    def list_clients(self):
        """
        UI part of listing clients.
        :return:
        """
        print("Here is the list of clients:\n")
        for client in self.__client_service.list_clients():
            print(str(client))
        if len(self.__client_service.list_clients()) == 0:
            print("No clients to show!\n")
        print("\n")

    # 1.2
    def manage_books(self):
        """
        Menu for managing books.
        :return:
        """
        while True:
            print("What would you like to do?\n"
                  "[1] Add a book\n"
                  "[2] Remove a book\n"
                  "[3] Update a book\n"
                  "[4] List books\n"
                  "[5] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.add_book()
                elif command == '2':
                    self.remove_book()
                elif command == '3':
                    self.update_book()
                elif command == '4':
                    self.list_books()
                elif command == '5':
                    break
                else:
                    print("Error: Invalid command!")
            except ValidationException:
                print("Error: Invalid command!")

    # 1.2.1
    def add_book(self):
        """
        UI part of adding a book.
        :return:
        """
        try:
            print("Please enter the following information using syntax:\n"
                  "<ID> <Title> <author>\n")
            syntax = input("Enter information: ")
            syntax = syntax.split(" ")
            if len(syntax) == 3:
                if syntax[0].isdigit():
                    if syntax[2].isalpha():
                        if self.__book_service.check_book_id_unique(syntax[0]):
                            self.__book_service.add_book(syntax[0], syntax[1], syntax[2])
                            self.__undo_service.book_adding_operation(syntax[0], syntax[1], syntax[2])
                        else:
                            raise RepositoryException("\nError: book ID already exists!\n")
                else:
                    raise ValidationException("\nError: ID has to be a positive integer!\n")
            else:
                raise ValidationException("\nError: Invalid syntax!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("book added successfully!\n")

    # 1.2.2
    def remove_book(self):
        """
        UI part of removing a book.
        :return:
        """
        try:
            print("Please enter the ID of the book you want to remove:\n")
            book_id = input("Enter ID: ").strip()
            if book_id.isdigit():
                if not self.__book_service.can_remove_book(book_id):
                    raise RepositoryException("\nError: No book has the requested id!\n")
                else:
                    temp1 = self.__book_service.get_book_title(book_id)
                    temp2 = self.__book_service.get_book_author(book_id)
                    array = self.__book_service.remove_book(book_id)
                    if array is not None:
                        self.__undo_service.book_removing_operation(book_id, temp1, temp2, array)
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("book removed successfully!\n")

    # 1.2.3
    def update_book(self):
        """
        UI part of updating a book.
        :return:
        """
        try:
            print("Please enter the ID of the book you wish to update.\n")
            book_id = input("Enter ID: ").strip()
            if book_id.isdigit():
                if self.__book_service.can_update_book(book_id):
                    print("Please update the title and author of the book that has the requested ID.\n")
                    syntax = input("Enter information: ")
                    syntax = syntax.split(" ")
                    if len(syntax) == 2:
                        if syntax[1].isalpha():
                            self.__undo_service.book_updating_operation(book_id, syntax[0], syntax[1],
                                                                         self.__book_service.get_book_title(book_id),
                                                                         self.__book_service.get_book_author(
                                                                             book_id))
                            self.__book_service.update_book(book_id, syntax[0], syntax[1])
                    else:
                        raise ValidationException("\nError: Invalid syntax!\n")
                else:
                    raise RepositoryException("\nError: No book has the requested ID!\n")
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("book updated successfully!\n")

    # 1.2.4
    def list_books(self):
        """
        UI part of listing books.
        :return:
        """
        print("Here is the list of books:\n")
        for book in self.__book_service.list_books():
            print(str(book))
        if len(self.__book_service.list_books()) == 0:
            print("No books to show!\n")
        print("\n")

    # 2
    def rent_or_return_book(self):
        """
        Menu for renting or returning a book.
        :return:
        """
        while True:
            print("What would you like to do?\n"
                  "[1] Rent a book\n"
                  "[2] Return a book\n"
                  "[3] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.rent_book()
                elif command == '2':
                    self.return_book()
                elif command == '3':
                    break
                else:
                    print("Error: Invalid command!")
            except ValidationException:
                print("Error: Invalid command!")

    # 2.1
    def rent_book(self):
        """
        UI part of renting a book.
        :return:
        """
        try:
            print("Please enter the following information using syntax:\n"
                  "<Client ID> <book ID>\n")
            syntax = input("Enter information: ")
            syntax = syntax.split(" ")
            if len(syntax) == 2:
                if syntax[0].isdigit():
                    if syntax[1].isdigit():
                        if self.__client_service.check_client_id(syntax[0]):
                            if self.__book_service.check_book_id(syntax[1]):
                                        self.__rental_service.rent_book(syntax[0], syntax[1])
                                        last_rental = self.__rental_service.get_last_rental()
                                        self.__undo_service.rental_adding_operation(last_rental.rental_id(),
                                                                                    last_rental.book_id(),
                                                                                    last_rental.client_id(),
                                                                                    last_rental.rented_date(),
                                                                                    last_rental.returned_date())
                            else:
                                raise RepositoryException("\nError: book ID does not exist!\n")
                        else:
                            raise RepositoryException("\nError: Client ID does not exist!\n")
                    else:
                        raise ValidationException("\nError: book ID has to be a positive integer!\n")
                else:
                    raise ValidationException("\nError: Client ID has to be a positive integer!\n")
            else:
                raise ValidationException("\nError: Invalid syntax!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("book rented successfully!\n")

    # 2.2
    def return_book(self):
        """
        UI part of returning a book.
        :return:
        """
        try:
            print("Please enter the rental ID of the book you want to return:\n")
            syntax = input("Enter ID: ").strip()
            if syntax.isdigit():
                if self.__rental_service.check_rental_id(syntax):
                    if self.__rental_service.check_returned_date(syntax):
                        needed_rental = self.__rental_service.get_rental(syntax)
                        self.__undo_service.rental_removing_operation(needed_rental.rental_id(),
                                                                      needed_rental.book_id(),
                                                                      needed_rental.client_id(),
                                                                      needed_rental.rented_date(),
                                                                      needed_rental.returned_date())
                        self.__rental_service.return_book(syntax)
                    else:
                        raise ValidationException("\nError: book has already been returned!\n")
                else:
                    raise RepositoryException("\nError: Rental ID does not exist!\n")
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)
        else:
            print("book returned successfully!\n")

    # 3
    def search(self):
        """
        Menu for searching.
        :return:
        """
        while True:
            print("What would you like to search?\n"
                  "[1] Clients\n"
                  "[2] books\n"
                  "[3] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.search_clients()
                elif command == '2':
                    self.search_books()
                elif command == '3':
                    break
                else:
                    print("Error: Invalid command!")
            except ValidationException:
                print("Error: Invalid command!")

    # 3.1
    def search_clients(self):
        """
        Menu for searching clients.
        :return:
        """
        while True:
            print("What would you like to search by?\n"
                  "[1] ID\n"
                  "[2] Name\n"
                  "[3] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.search_clients_by_id()
                elif command == '2':
                    self.search_clients_by_name()
                elif command == '3':
                    break
                else:
                    print("Error: Invalid command!")
            except ValidationException:
                print("Error: Invalid command!")

    # 3.1.1
    def search_clients_by_id(self):
        """
        UI part of searching clients by ID.
        :return:
        """
        try:
            print("Please enter the ID of the client you want to search for:\n")
            client_id = input("Enter ID: ").strip()
            if client_id.isdigit():
                if len(self.__client_service.search_client_by_id(client_id)) == 0:
                    print("No clients to show!\n")
                else:
                    print("Here is the list of clients:\n")
                    for client in self.__client_service.search_client_by_id(client_id):
                        print(str(client))
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)

    # 3.1.2
    def search_clients_by_name(self):
        """
        UI part of searching clients by name.
        :return:
        """
        print("Please enter the name of the client you want to search for:\n")
        client_name = input("Enter name: ")
        if len(self.__client_service.search_client_by_name(client_name)) == 0:
            print("No clients to show!\n")
        else:
            print("Here is the list of clients:\n")
            for client in self.__client_service.search_client_by_name(client_name):
                print(str(client))

    # 3.2
    def search_books(self):
        """
        Menu for searching books.
        :return:
        """
        while True:
            print("What would you like to search by?\n"
                  "[1] ID\n"
                  "[2] Title\n"
                  "[3] author\n"
                  "[4] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.search_books_by_id()
                elif command == '2':
                    self.search_books_by_title()
                elif command == '3':
                    self.search_books_by_author()
                elif command == '4':
                    break
                else:
                    print("Error: Invalid command!")
            except ValidationException:
                print("Error: Invalid command!")

    # 3.2.1
    def search_books_by_id(self):
        """
        UI part of searching books by ID.
        :return:
        """
        try:
            print("Please enter the ID of the book you want to search for:\n")
            book_id = input("Enter ID: ").strip()
            if book_id.isdigit():
                if len(self.__book_service.search_book_by_id(book_id)) == 0:
                    print("No books to show!\n")
                else:
                    print("Here is the list of books:\n")
                    for book in self.__book_service.search_book_by_id(book_id):
                        print(str(book))
            else:
                raise ValidationException("\nError: ID has to be a positive integer!\n")
        except ValidationException as ve:
            print(ve)

    # 3.2.2
    def search_books_by_title(self):
        """
        UI part of searching books by title.
        :return:
        """
        print("Please enter the title of the book you want to search for:\n")
        book_title = input("Enter title: ")
        if len(self.__book_service.search_book_by_title(book_title)) == 0:
            print("No books to show!\n")
        else:
            print("Here is the list of books:\n")
            for book in self.__book_service.search_book_by_title(book_title):
                print(str(book))

    # 3.2.3
    def search_books_by_author(self):
        """
        UI part of searching books by author.
        :return:
        """
        print("Please enter the author of the book you want to search for:\n")
        book_author = input("Enter author: ")
        if len(self.__book_service.search_book_by_author(book_author)) == 0:
            print("No books to show!\n")
        else:
            print("Here is the list of books:\n")
            for book in self.__book_service.search_book_by_author(book_author):
                print(str(book))


    # 4
    def statistics(self):
        """
        Menu for statistics.
        :return:
        """
        while True:
            print("What would you like to see?\n"
                  "[1] Most rented books\n"
                  "[2] Most active clients\n"
                  "[3] Most rented author\n"
                  "[4] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.most_rented_books()
                elif command == '2':
                    self.most_active_clients()
                elif command == '3':
                    self.most_rented_authors()
                elif command == '4':
                    break
                else:
                    print("Error: Invalid command!")
            except ValidationException:
                print("Error: Invalid command!")

    # 4.1
    def most_rented_books(self):
        """
        UI part of most rented books.
        :return:
        """
        print("Here is the list of most rented books:\n")
        for book, count in self.__rental_service.most_rented_books():
            print(book.title() + " - " + str(count) + " rentals")
        print("\n")

    # 4.2
    def most_active_clients(self):
        """
        UI part of most active clients.
        :return:
        """
        print("Here is the list of most active clients:\n")
        for client, count in self.__rental_service.most_active_clients():
            print(client + " - " + str(count) + " rentals")
        print("\n")

    # 4.3
    def most_rented_authors(self):
        """
        UI part for displaying most rented authors
        """
        print("Here is the list of most rented authors:\n")
        authors = self.__rental_service.most_rented_authors()
        for author, count in authors:
            print(f"{author} - {count} rentals")
        print("\n")

    # 5
    def undo_menu(self):
        while True:
            print("What operation would you like to perform?\n"
                  "[1] Undo\n"
                  "[2] Redo\n"
                  "[3] Back\n")
            try:
                command = input("Enter command: ").strip()
                if command == '1':
                    self.undo()
                elif command == '2':
                    self.redo()
                elif command == '3':
                    break
                else:
                    raise ValidationException("Error: Invalid command!")
            except ValidationException as ve:
                print(ve)

    def undo(self):
        try:
            self.__undo_service.undo()
        except UndoRedoException as ure:
            print(ure)
        else:
            print("Operation undone successfully!\n")

    def redo(self):
        try:
            self.__undo_service.redo()
        except UndoRedoException as ure:
            print(ure)
        else:
            print("Operation redone successfully!\n")
