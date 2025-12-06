class TeamRepo:
    def __init__(self):
        self._teams = set()

    def add_team(self, team):
        """Adaugă o echipă în set."""
        if team in self._teams:
            raise ValueError(f"Echipa cu id-ul {team} există deja!")
        self._teams.add(team)

    def get_all_teams(self):
        """Returnează toate echipele."""
        return list(self._teams)

    def team_exists(self, id_team):
        """Verifică dacă o echipă cu un anumit id_team există."""
        return id_team in self._teams