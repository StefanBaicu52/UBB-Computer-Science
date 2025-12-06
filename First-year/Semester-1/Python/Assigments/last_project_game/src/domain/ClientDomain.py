class Client:
    def __init__(self, client_id, client_name):
        self.__client_id = client_id
        self.__client_name = client_name

    def client_id(self):
        return self.__client_id

    def client_name(self):
        return self.__client_name

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def __str__(self):
        return "#" + str(self.__client_id) + " " + str(self.__client_name)