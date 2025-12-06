from src.domain.BookDomain import Book


class BookService:
    def __init__(self, book_repository):
        """
        Constructor for BookService class
        :param book_repository:
        """
        self.__book_repository = book_repository

    def add_book(self, book_id, title, author):
        """
        Adds a book to the repository
        :param book_id:
        :param title:
        :param author:
        :return:
        """
        book = Book(book_id, title, author)
        self.__book_repository.add_book(book)

    def check_book_id_unique(self, book_id):
        """
        Checks if a book ID is unique
        :param book_id:
        :return:
        """
        for book in self.__book_repository.get_all_books():
            if book.book_id() == book_id:
                return False
        return True

    def remove_book(self, book_id):
        """
        Removes a book from the repository
        :param book_id:
        :return:
        """
        self.__book_repository.remove_book(book_id)

    def can_remove_book(self, book_id):
        """
        Checks if a book can be removed from the repository
        :param book_id:
        :return:
        """
        for book in self.__book_repository.get_all_books():
            if book.book_id() == book_id:
                return True
        return False

    def update_book(self, book_id, title, author):
        """
        Updates a book from the repository
        :param book_id:
        :param title:
        :param author:
        :return:
        """
        self.__book_repository.update_book(book_id, title, author)

    def can_update_book(self, book_id):
        """
        Checks if a book can be updated from the repository
        :param book_id:
        :return:
        """
        for book in self.__book_repository.get_all_books():
            if book.book_id() == book_id:
                return True
        return False

    def list_books(self):
        """
        Returns the list of books
        :return:
        """
        return self.__book_repository.list_books()

    def check_book_id(self, book_id):
        """
        Checks if a book ID exists
        :param book_id:
        :return:
        """
        return self.__book_repository.check_book_id(book_id)

    def search_book_by_id(self, book_id):
        """
        Searches for a book by ID
        :param book_id:
        :return:
        """
        return self.__book_repository.search_book_by_id(book_id)

    def search_book_by_title(self, title):
        """
        Searches for a book by title
        :param title:
        :return:
        """
        return self.__book_repository.search_book_by_title(title)

    def search_book_by_author(self, author):
        """
        Searches for a book by description
        :param author:
        :return:
        """
        return self.__book_repository.search_book_by_author(author)

    def get_book_title(self, book_id):
        """
        Gets the book title
        :param book_id:
        :return:
        """
        return self.__book_repository.get_book_title(book_id)

    def get_book_author(self, book_id):
        """
        Gets the book author
        :param book_id:
        :return:
        """
        return self.__book_repository.get_book_author(book_id)



