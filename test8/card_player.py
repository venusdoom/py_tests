# A module for a simple game


class CardPlayer:
    """Describes a card player as object"""

    def __init__(self, name, score=0):
        self.name = name
        self.cards = []
        self.score = score

    def __str__(self):
        rep = "\tName: " + self.name + "\n\tCards: " + ', '.join(map(str, self.cards)) + "\n\tScore: " + str(self.score)
        return rep


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

