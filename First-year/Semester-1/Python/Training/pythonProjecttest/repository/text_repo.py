from repository.team_repo import TeamRepo
from domain.team_domain import TeamDomain

class FileTeamRepo(TeamRepo):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.load()  # Load teams when initializing the repository

    def save(self):
        """Save the teams to the file."""
        with open(self.file_path, 'w') as f:
            for team in self._teams:
                f.write(f"{team.team_id},{team.team_name}\n")  # Save team_id and team_name separated by '|'

    def load(self):
        """Load the teams from the file."""
        try:
            with open(self.file_path, 'r') as f:
                self._teams = {
                    TeamDomain(*line.strip().split(',')) for line in f
                }  # Split each line into team_id and team_name and create Team objects
        except FileNotFoundError:
            self._teams = set()  # If the file doesn't exist, initialize with an empty set.

    def add_team(self, team):
        """Adaugă o echipă în set."""
        super().add_team(team)  # Call the parent method to add a team.

    def get_all_teams(self):
        """Returnează toate echipele."""
        return super().get_all_teams()  # Call the parent method to get all teams.

    def team_exists(self, id_team):
        """Verifică dacă o echipă cu un anumit id_team există."""
        return super().team_exists(id_team)  # Call the parent method to check if a team exists.
