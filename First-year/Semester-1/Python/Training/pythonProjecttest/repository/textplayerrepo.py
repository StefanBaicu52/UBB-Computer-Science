from domain.player import Player
from repository.player_repo import PlayerRepo
class PlayerTextRepo(PlayerRepo):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(Pla, player):
        with open(self.file_path, 'a') as f:
            f.write(f"{player.id_player},{player.team_id},{player.player_name}\n")

    def load(self):
        players = []
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    id_player, team_id, player_name = line.strip().split(',')
                    players.append(Player(id_player, team_id, player_name))
        except FileNotFoundError:
            pass  # Dacă fișierul nu există, returnează lista goală.
        return players

    def add_player(self, player):
        return super().add_player(player)
