class Book:
    def __init__(self,book_id,title,author):
        self.__book_id=book_id
        self.__book_title=title
        self.__book_author=author

    def book_id(self):
        return self.__book_id

    def book_title(self):
        return self.__book_title

    def book_author(self):
        return self.__book_author

    def set_book_title(self,title):
        self.__book_title=title

    def set_book_author(self,author):
        self.__book_author=author

    def __str__(self):
        return "#" + str(self.__book_id) + " " + str(self.__book_title) + str(self.__book_author)