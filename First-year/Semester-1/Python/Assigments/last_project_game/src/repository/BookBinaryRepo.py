from src.repository.BookRepo import BookRepo
from src.domain.BookDomain import Book
import pickle


class BookBinaryRepo(BookRepo):
    def __init__(self, file, rental_repo):
        super().__init__(rental_repo)
        self._file = file
        self._book_data = self._load_from_file()

    def add_book(self, book):
        super().add_book(book)
        self._save_to_file()

    def remove_book(self, book_id):
        result = super().remove_book(book_id)
        self._save_to_file()
        return result

    def update_book(self, book_id, title, author):
        super().update_book(book_id, title, author)
        self._save_to_file()

    def _save_to_file(self):
        file = open(self._file, "wb")
        pickle.dump(self._book_data, file)
        file.close()

    def _load_from_file(self):
        try:
            file = open(self._file, "rb")
            temp_data = pickle.load(file)
            file.close()
            return temp_data
        except:
            # If any issue occurs (like the file doesn't exist or is empty),
            # return an empty list.
            return []
