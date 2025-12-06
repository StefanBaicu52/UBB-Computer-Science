from Controller import QuestionController
from Repository import QuestionRepository
from Domain import Question
import random

class UI:

    def __init__(self, controller):
        self.controller = controller

    def read_command(self):
        cmd = input()
        cmd = cmd.split(" ", 1)
        if cmd[0] == "add":
            self.add_question(cmd[1])
        elif cmd[0] == "create":
            self.create_question(cmd[1])
        elif cmd[0] == "start":
            self.start_quiz(cmd[1])
        elif cmd[0] == "exit":
            return "break"
        elif cmd[0] == "display":
            self.display()
        else:
            print("There is no such command!")
            return False

    def add_question(self, parameters):
        params = parameters.split(";")
        if len(params) != 7:
            print("The format is wrong!")
            return False
        else:
            question_id = params[0]
            text = params[1]
            answer1 = params[2]
            answer2 = params[3]
            answer3 = params[4]
            correct_answer = params[5]
            difficulty = params[6]
            q = Question(question_id, text, answer1, answer2, answer3, correct_answer, difficulty)
            self.controller.repo.add_question(q)
            print("Question added")
            return True

    def create_question(self, parameters):
        params = parameters.split(" ")
        if len(params) != 3:
            print("The format is wrong!")
            return False
        else:
            params[1] = int(params[1])
            if params[1] > len(self.controller.repo.data):
                print("The number you provided is larger than the number of questions available!")
                return False
            else:
                if int(params[1])/2 > self.controller.count_questions(params[0]):
                    print("The number of questions with this level of difficulty is not enough!")
                else:
                    questions = self.controller.get_questions_of_difficulty(params[0], params[1])
                    self.controller.writetofile(params[2], questions)
                    print("Quiz created")
                    return True

    def start_quiz(self, parameters):
        questions = self.controller.readquizfromfile(parameters)
        questions_to_delete = []
        score = 0
        for q in questions:
            print(q.getdifficulty())
            if q.getdifficulty() == "easy":
                print(q.gettext())
                answers = q.getanswers()
                for a in range(len(answers)):
                    print(str(a+1) + ")" + str(answers[a]))
                answer = input()
                if answer == q.getcorrectanswer():
                    score += 1
                questions_to_delete.append(q)
        for q in questions_to_delete:
            questions.remove(q)
        questions_to_delete = []
        for q in questions:
            if q.getdifficulty() == "medium":
                print(q.gettext())
                answers = q.getanswers()
                for a in range(len(answers)):
                    print(str(a+1) + ")" + str(answers[a]))
                answer = input()
                if answer == q.getcorrectanswer():
                    score += 2
                questions_to_delete.append(q)
        for q in questions_to_delete:
            questions.remove(q)
        for q in questions:
            if q.getdifficulty() == "hard":
                print(q.gettext())
                answers = q.getanswers()
                for a in range(len(answers)):
                    print(str(a+1) + ")" + str(answers[a]))
                answer = input()
                if answer == q.getcorrectanswer():
                    score += 3
                questions_to_delete.append(q)
        print(score)
        return True

    def display(self):
        for i in self.controller.repo.data:
            print(i)
        return True

    def Menu(self):

        rsp = self.read_command()
        while rsp != "break":
            rsp = self.read_command()

Repo = QuestionRepository()
q1 = Question("1", "Which number is the biggest?", "1", "4", "3", "4", "easy")
Repo.add_question(q1)
q2 = Question("2", "Which number is the smallest?", "-3", "3", "0", "-3", "easy")
Repo.add_question(q2)
q3 = Question("3", "Which number is prime?", "2", "32", "9", "2", "easy")
Repo.add_question(q3)
q4 = Question("4", "Which country has the largest GDP?", "Brazil", "China", "UK", "China", "medium")
Repo.add_question(q4)
q5 = Question("5", "Which is not a fish?", "carp", "orca", "eel", "orca", "medium")
Repo.add_question(q5)
q6 = Question("6", "Name the first satellite:", "Apollo", "Sputnik", "Zaria", "Sputnik", "medium")
Repo.add_question(q6)
q7 = Question("7", "Which Apollo mission did not make it to the Moon?", "11", "13", "17", "13", "hard")
Repo.add_question(q7)
q8 = Question("8", "A mole can be a:", "animal", "quantity", "both", "both", "hard")
Repo.add_question(q8)
q9 = Question("9", "Name El Cid's horse:", "Babieca", "Abu", "Santiago", "Babieca", "hard")
Repo.add_question(q9)
q10 = Question("10", "The Western Roman Empire fell in:", "654", "546", "476", "476", "hard")
Repo.add_question(q10)
Ctrl = QuestionController(Repo)
ui = UI(Ctrl)
ui.Menu()