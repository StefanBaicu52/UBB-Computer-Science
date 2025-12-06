class Question:

    def __init__(self, question_id, text, answer1, answer2, answer3, correct_answer, difficulty):
        self.question_id = question_id
        self.text = text
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct_answer = correct_answer
        self.difficulty = difficulty

    def __str__(self):
        string = str(self.question_id) + ";" + str(self.text) + ";" + str(self.answer1)
        string = string + ";" + str(self.answer2) + ";" + str(self.answer3) + ";" + str(self.correct_answer)
        string = string + ";" + str(self.difficulty)
        return string

    def getquestion_id(self):
        return self.question_id

    def gettext(self):
        return self.text

    def getanswers(self):
        return self.answer1, self.answer2, self.answer3

    def getcorrectanswer(self):
        return self.correct_answer

    def getdifficulty(self):
        return self.difficulty

# string = "adgxd safdsg rgeh tr"
# string = string.split(" ", 1)
# print(string)
# string2 = string[1]
# string2 = string2.split(" ")
# print(string2)