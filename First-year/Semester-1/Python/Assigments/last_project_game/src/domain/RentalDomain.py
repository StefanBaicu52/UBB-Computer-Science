class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    def rental_id(self):
        return self.__rental_id

    def book_id(self):
        return self.__book_id

    def client_id(self):
        return self.__client_id

    def rented_date(self):
        return self.__rented_date

    def returned_date(self):
        return self.__returned_date

    def set_returned_date(self, returned_date):
        self.__returned_date=returned_date