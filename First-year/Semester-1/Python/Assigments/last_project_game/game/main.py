from game.controller.game_controller import GameController
from game.ui.ui_console import ConsoleView

if __name__ == "__main__":
    controller = GameController()
    ui = ConsoleView(controller)
    ui.play_game()