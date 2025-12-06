from service.team_service import TeamService
from repository.team_repo import TeamRepo
from repository.text_repo import FileTeamRepo
from ui.ui import UI

if __name__ == "__main__":


    repo = FileTeamRepo("team.txt")
    service = TeamService(repo)
    ui = UI(service)


    #echipe pt teste=
    service.add_team("1", "Barcelona")
    service.add_team("2", "Real")
    service.add_team("3", "Manchester United")



    ui.run()