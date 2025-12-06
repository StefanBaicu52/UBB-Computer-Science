class Player:
    def __init__(self,id_player, team_id, player_name):
        self.__id_player = id_player
        self.__team_id = team_id
        self.__player_name = player_name

    @property
    def id_player(self):
        return self.__id_player

    @property
    def team_id(self):
        return self.__team_id

    @property
    def player_name(self):
        return self.__player_name

    def __str__(self):
        return f"Id:ID:{self.__id_player}  Team: {self.__team_id}, Name: {self.__player_name}"

