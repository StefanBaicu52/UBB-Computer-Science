from src.repository.BookRepo import BookRepo
from src.domain.BookDomain import Book

class BookTextRepo(BookRepo):
    def __init__(self, file, rental_repo):
        """
        Constructor for BookTextRepo.
        Initializes the repository with data loaded from a text file.
        :param file: Path to the text file.
        :param rental_repo: Reference to the rental repository.
        """
        super().__init__(rental_repo)
        self._file = file
        self._book_data = self.load_from_file(self._file) or []

    def add_book(self, book):
        """
        Adds a book to the repository and saves it to the file.
        :param book: Book object to add.
        """
        super().add_book(book)
        self.save_to_file(self._file)

    def remove_book(self, book_id):
        """
        Removes a book from the repository and updates the file.
        :param book_id: ID of the book to remove.
        :return: The removed book object, or None if not found.
        """
        result = super().remove_book(book_id)
        self.save_to_file(self._file)
        return result

    def update_book(self, book_id, title, author):
        """
        Updates a book's information in the repository and file.
        :param book_id: ID of the book to update.
        :param title: New title of the book.
        :param author: New author of the book.
        """
        super().update_book(book_id, title, author)
        self.save_to_file(self._file)

    def list_books(self):
        """
        Returns the list of books.
        :return: List of books.
        """
        return super().list_books()

    def check_book_id(self, book_id):
        """
        Checks if a book ID exists in the repository.
        :param book_id: Book ID to check.
        :return: True if the book ID exists, False otherwise.
        """
        return super().check_book_id(book_id)

    def search_book_by_id(self, book_id):
        """
        Searches for a book by its ID.
        :param book_id: ID of the book to search.
        :return: The book object if found, None otherwise.
        """
        return super().search_book_by_id(book_id)

    def search_book_by_title(self, title):
        """
        Searches for books by title.
        :param title: Title to search for.
        :return: List of books matching the title.
        """
        return super().search_book_by_title(title)

    def search_book_by_author(self, author):
        """
        Searches for books by author.
        :param author: Author to search for.
        :return: List of books matching the author.
        """
        return super().search_book_by_author(author)

    def get_all_books(self):
        """
        Returns all books in the repository.
        :return: List of all books.
        """
        return super().get_all_books()

    def get_book_title(self, book_id):
        """
        Gets the title of a book by its ID.
        :param book_id: ID of the book.
        :return: Title of the book.
        """
        return super().get_book_title(book_id)

    def get_book_author(self, book_id):
        """
        Gets the author of a book by its ID.
        :param book_id: ID of the book.
        :return: Author of the book.
        """
        return super().get_book_author(book_id)

    def save_to_file(self, textfile):
        """
        Saves the current book data to the text file.
        :param textfile: Path to the text file.
        """
        try:
            with open(textfile, "w") as file:
                for book in self._book_data:
                    file.write(f"{book.book_id()},{book.book_title()},{book.book_author()}\n")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, textfile):
        """
        Loads book data from the text file.
        :param textfile: Path to the text file.
        :return: List of Book objects.
        """
        try:
            temp_data = []
            with open(textfile, "r") as file:
                for line in file:
                    line = line.strip()
                    parts = line.split(",")
                    if len(parts) == 3:  # Ensure valid data format
                        temp_data.append(Book(parts[0], parts[1], parts[2]))
            return temp_data
        except FileNotFoundError:
            print(f"File not found: {textfile}. Returning empty data.")
            return []
        except Exception as e:
            print(f"Error loading from file: {e}")
            return []
