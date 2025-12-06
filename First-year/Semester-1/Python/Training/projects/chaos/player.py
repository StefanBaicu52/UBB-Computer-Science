class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return f"{self.name} ({self.token})"

    def get_token(self):
        return self.token