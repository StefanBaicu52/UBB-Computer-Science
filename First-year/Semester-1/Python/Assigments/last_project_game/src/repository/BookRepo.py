from src.domain.BookDomain import Book
from src.exceptions.Exceptions import RepositoryException


class BookRepo:
    def __init__(self,rental_repo):
        """
        Creates a new instance of bookRepo
        """
        self.__book_data = []
        self._rental_repo=rental_repo
        for count in range(1, 21):
            self.__book_data.append(Book(str(count), "book" + str(count), "Author"
                                           + str(count)))

    def add_book(self, book):
        """
        Adds a book to the repository
        :param book: book
        :return: None
        """
        for book_inlist in self.__book_data:
            if book_inlist.book_id() == book.book_id():
                raise RepositoryException("book ID already exists!\n")
        self.__book_data.append(book)

    def remove_book(self, book_id):
        """
        Removes a book from the repository
        :param book_id: int
        :return: None
        """
        array=[]
        for book in self.__book_data:
            if book.book_id() == book_id:
                self.__book_data.remove(book)
                for rental in self._rental_repo.list_rentals():
                    self._rental_repo.remove(rental.rental_id)
                    array.append(rental)
        return array

    def update_book(self, book_id, title, author):
        """
        Updates a book from the repository
        :param book_id: int
        :param title: string
        :param author: string
        :return: None
        """
        for book in self.__book_data:
            if book.book_id() == book_id:
                book.set_book_title(title)
                book.set_book_author(author)
                return  # Update successful, return early
        raise RepositoryException(f"Book with ID {book_id} not found.")  # Throw error if not found

    def list_books(self):
        """
        Returns the list of books
        :return: list
        """
        return self.__book_data

    def check_book_id(self, book_id):
        """
        Checks if the book ID exists
        :param book_id: int
        :return: bool
        """
        for book in self.__book_data:
            if book.book_id() == book_id:
                return True

    def search_book_by_id(self, book_id):
        """
        Searches for a book by ID
        :param book_id: int
        :return: book
        """
        book_list = []
        for book in self.__book_data:
            if book_id in book.book_id():
                book_list.append(book)

        return book_list

    def search_book_by_title(self, title):
        """
        Searches for a book by title
        :param title: string
        :return: book
        """
        book_list = []
        for book in self.__book_data:
            if title.lower() in book.book_title().lower():
                book_list.append(book)

        return book_list

    def search_book_by_author(self, author):
        """
        Searches for a book by author
        :param author: string
        :return: book
        """
        book_list = []
        for book in self.__book_data:
            if author.lower() in book.book_author().lower():
                book_list.append(book)

        return book_list


    def get_all_books(self):
        return self.__book_data

    def get_book_title(self, book_id):
        for book in self.__book_data:
            if book.book_id() == book_id:
                return book.book_title()

    def get_book_author(self, book_id):
        for book in self.__book_data:
            if book.book_id() == book_id:
                return book.book_author()

