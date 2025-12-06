class TeamDomain:
    def __init__(self, team_id, team_name):
        self.__team_id = team_id
        self.__team_name = team_name

    @property
    def team_id(self):
        return self.__team_id

    @property
    def team_name(self):
        return self.__team_name

    def __str__(self):
        return f"Id: {self.__team_id}, Name: {self.__team_name}"

