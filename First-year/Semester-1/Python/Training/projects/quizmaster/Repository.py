class QuestionRepository:

    def __init__(self):
        self.data = []

    def add_question(self, question):
        self.data.append(question)
