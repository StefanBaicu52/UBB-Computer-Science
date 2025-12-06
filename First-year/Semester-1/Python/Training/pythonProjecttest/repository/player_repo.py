class PlayerRepo:
    def __init__(self):
        self._players = {}

    def add_player(self, player):
        if player.id_player in self._players:
            raise ValueError(f"Jucătorul cu ID-ul {player.id_player} există deja.")
        self._players[player.id_player] = player

    def get_player(self, id_player):
        return self._players.get(id_player)

    def player_exists(self, id_player):
        return id_player in self._players
