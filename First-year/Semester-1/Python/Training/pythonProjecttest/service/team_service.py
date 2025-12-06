from domain.team_domain import TeamDomain

class TeamService:
    def __init__(self, repository):
        self.__repo = repository

    def add_team(self, team_id, team_name):
        team= TeamDomain(team_id, team_name)
        self.__repo.add_team(team)

    def get_all_teams(self):
        return self.__repo.get_all_teams()

