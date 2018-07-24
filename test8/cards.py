# A module for standard card deck


class UsualCardSet:
    """Describes a standard card"""

    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = self.suit + "-" + self.rank
        return rep

    @property
    def value(self):
        if self.rank == "Ace":
            v = 1
        elif self.rank in ("Jack", "Queen", "King"):
            v = 10
        elif not self.rank:
            v = None
        else:
            v = int(self.rank)
        return v


class Deck:
    """Describes a deck object as a set of card objects"""

    def __init__(self):
        self.deck = []

    def __str__(self):
        rep = ', '.join(map(str, self.deck))
        return rep

    def create_deck(self, card_set):
        for rank in card_set.RANKS:
            for suit in card_set.SUITS:
                self.deck.append(card_set(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.deck)
        print("\nThe deck was shuffled.")

    def give_card(self, player, number=1):
        if self.deck:
            for i in range(number):
                print("Giving some card from deck to", player.name)
                player.cards.append(self.deck[0])
                player.score += self.deck[0].value
                del self.deck[0]
        else:
            print("No cards in deck.")


# debug!
card_set = UsualCardSet()
print(card_set.SUITS)
deck = Deck()
deck += card_set
#deck.create_deck(card_set)
print("\n", "New deck:\n", deck)
# debug!

# debug!
debug = False
if debug:
    card = UsualCardSet("S", "2")
    print("Predefined card:", card)
    print("Value of predefined card:", card.value)

    deck = Deck()
    deck.create_deck(UsualCardSet)
    print("\n", "New deck:\n", deck)

    deck.shuffle()
    print("\n", "Shuffled deck:\n", deck)

    import test8.card_player

    player1 = test8.card_player.CardPlayer("John")
    player2 = test8.card_player.CardPlayer("Bill")
    players = [player1, player2]

    print("\nDealing deck to players:")
    while deck.deck:
        for player in players:
            deck.give_card(player, 2)

    print("\n", player1)
    print("\n", player2)
    print("\n", "Deck after dealing:\n", deck)
# debug!