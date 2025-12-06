from service.team_service import TeamService

class UI:
    def __init__(self,service):
        self.__task_service = service

    def t_menu(self):
        print("\nHello! This is the menu\n"
              "add-team\n"
              "list-teams\n"
              "exit\n")

    def run(self):
        while True:
            self.t_menu()
            command = input("enter command: ").strip()
            parts = command.split(" ")
            if parts[0] == "add-team" and len(parts) == 3:
                team_id = parts[1]
                team_name = parts[2]
                self.__task_service.add_team(team_id, team_name)
                print(f"added team {team_id} {team_name}")
            elif parts[0] == "list-teams":
                teams = self.__task_service.get_all_teams()
                for team in teams:
                    print(f"ID: {team.team_id}, Nume: {team.team_name}")
            elif parts[0] == "exit":
                break
            else:
                print("invalid command")




