from src.repository.ClientRepo import ClientRepo
from src.domain.ClientDomain import Client

class ClientTextRepo(ClientRepo):
    def __init__(self, file, rental_repo):
        super().__init__(rental_repo)
        self._file = file
        self._client_data = self.load_from_file(self._file)

    def add_client(self, client):
        """
        Adds a client to the list and saves to file.
        """
        super().add_client(client)
        self._client_data.append(client)  # Update in-memory list
        print(f"Client added: {client.client_id()} - {client.client_name()}")
        self.save_to_file(self._file)

    def check_client_id(self, client_id):
        return super().check_client_id(client_id)

    def search_client_by_id(self, client_id):
        return super().search_client_by_id(client_id)

    def search_client_by_name(self, client_name):
        return super().search_client_by_name(client_name)

    def remove_client(self, client_id):
        """
        Removes a client by ID and updates the file.
        """
        client_to_remove = None
        for client in self._client_data:
            if client.client_id() == client_id:
                client_to_remove = client
                break
        if client_to_remove:
            self._client_data.remove(client_to_remove)  # Update in-memory list
            print(f"Client removed: {client_to_remove.client_id()} - {client_to_remove.client_name()}")
            super().remove_client(client_id)  # Call the base method for removal
            self.save_to_file(self._file)
            return True
        return False

    def update_client(self, client_id, client_name):
        """
        Updates a client's name and saves the updated list to the file.
        """
        updated = False
        for client in self._client_data:
            if client.client_id() == client_id:
                old_name = client.client_name()  # Store the old name for logging
                client._name = client_name  # Update client's name
                updated = True
                print(f"Client updated: {client_id} from {old_name} to {client_name}")
                break
        if updated:
            super().update_client(client_id, client_name)
            self.save_to_file(self._file)

    def list_clients(self):
        print("Listing all clients:")
        for client in self._client_data:
            print(f"  {client.client_id()} - {client.client_name()}")
        return super().list_clients()

    def get_client_name(self, client_id):
        return super().get_client_name(client_id)

    def save_to_file(self, textfile):
        """
        Saves all client data to the specified file.
        """
        try:
            with open(textfile, "w") as file:
                for client in self._client_data:
                    file.write(f"{client.client_id()},{client.client_name()}\n")
                print(f"Data saved to {textfile}:")
                for client in self._client_data:
                    print(f"  {client.client_id()} - {client.client_name()}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, textfile):
        """
        Loads client data from the file into the in-memory list.
        If the file doesn't exist, it creates an empty file.
        """
        try:
            temp_data = []
            try:
                with open(textfile, "r") as file:
                    for line in file:
                        line = line.strip()
                        line = line.split(",")
                        temp_data.append(Client(line[0], line[1]))  # Create client objects
            except FileNotFoundError:
                with open(textfile, "w"):  # Create the file if it doesn't exist
                    pass
            return temp_data
        except Exception as e:
            print(f"Error loading from file: {e}")
            return []
