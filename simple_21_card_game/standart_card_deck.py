# A module for standard card deck


class Card:
    """Describes a standard card"""

    SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
    RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = self.suit + self.rank
        return rep


class Deck(Card):
    """Describes a deck of standard cards"""

    def __init__(self):
        super().__init__()
        self.deck = []

    def __str__(self):
        rep = ', '.join(map(str, self.deck))
        return rep

    def create_deck(self):
        for rank in Deck.RANKS:
            for suit in Deck.SUITS:
                self.deck.append(suit + rank)

    def shuffle(self):
        import random
        random.shuffle(self.deck)


card = Card("A", "S")
print(card)

deck = Deck()
deck.create_deck()
print("\n", deck)

deck.shuffle()
print("\n", deck)
