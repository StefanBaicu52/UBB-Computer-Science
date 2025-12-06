from service import Services
from memory_repository import MemRepo
from text_file_repository import TextRepo
from binary_repository import BinaryRepo
from ui import UI

if __name__ == "__main__":
    # Initialize repository and service
    repository = BinaryRepo()
    service = Services(repository)
    # Start the UI
    ui = UI(service)
    ui.start()


