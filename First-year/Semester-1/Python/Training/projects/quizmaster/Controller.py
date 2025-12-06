from Repository import QuestionRepository
from Domain import Question
import random

class QuestionController:

    def __init__(self, repo):
        self.repo = repo

    def get_questions_of_difficulty(self, difficulty, n):
        list_of_questions = []
        list_of_questions_of_difficulty = []
        for i in self.repo.data:
            if i.getdifficulty() == difficulty:
                list_of_questions_of_difficulty.append(i)
        i = 0
        while i < n/2:
            a = random.choice(list_of_questions_of_difficulty)
            if a not in list_of_questions:
                list_of_questions.append(a)
                i += 1

        while i < n:
            a = random.choice(self.repo.data)
            if a not in list_of_questions:
                list_of_questions.append(a)
                i += 1

        return list_of_questions

    def count_questions(self, difficulty):
        n = 0
        for i in self.repo.data:
            if i.getdifficulty() == difficulty:
                n += 1
        return n

    def writetofile(self, fname, questionlist):

        with open(fname, 'w') as f:
            for i in range(len(questionlist)):
                f.write(str(questionlist[i]))
                f.write("\n")
        f.close()

    def readquizfromfile(self, fname):

        quiz = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for i in lines:
                i = i.strip("\n")
                i = i.split(";")
                id = i[0]
                text = i[1]
                answer1 = i[2]
                answer2 = i[3]
                answer3 = i[4]
                correct_answer = i[5]
                difficulty = i[6]
                q = Question(id, text, answer1, answer2, answer3, correct_answer, difficulty)
                quiz.append(q)
        f.close()
        return quiz



