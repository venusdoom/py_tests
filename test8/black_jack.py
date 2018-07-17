# Black Jack game example

import test8.cards
import test8.games


class BJCard(test8.cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v


class BJDeck(test8.cards.Deck):
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))


class BJHand(test8.cards.Hand):
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return 0
        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJPlayer(BJHand):
    def is_hitting(self):
        response = test8.games.ask_yes_no("\n" + self.name + ", need a card? (y/n): ")
        return response == "y"

    def bust(self):
        print(self.name, "overloaded.")
        self.lose()

    def lose(self):
        print(self.name, "out of game.")

    def win(self):
        print(self.name, "won.")

    def push(self):
        print(self.name, "draw.")


class BJDealer(BJHand):
    def is_hitting(self):
        response = test8.games.ask_yes_no("\n" + self.name + ", need a card? (y/n): ")
        return response == "y"
        # return self.total < 17

    def bust(self):
        print(self.name, "overloaded.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJGame:
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)

        self.dealer = BJDealer("Dealer")
        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal((self.players + [self.dealer]), per_hand=2)
        # self.dealer.flip_first_card()

        for player in self.players:
            self.__additional_cards(player)
            # self.dealer.flip_first_card()
            if not self.still_playing:
                print(self.dealer)
            else:
                print(self.dealer)
                self.__additional_cards(self.dealer)
                if self.dealer.is_busted():
                    for player in self.still_playing:
                        player.win()
                else:
                    for player in self.still_playing:
                        if player.total > self.dealer.total:
                            player.win()
                        elif player.total < self.dealer.total:
                            player.lose()
                        else:
                            player.push()

        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("Welcome to black jack card game.\n")
    names = []
    number = test8.games.ask_number("How many players (1-7)? ", low=1, high=8)
    for i in range(number):
        name = input("\nEnter player name: ")
        names.append(name)
        print()
    game = BJGame(names)
    again = None
    while again != "n":
        game.play()
        again = test8.games.ask_yes_no("\nDo you want to play again? ")


main()
input("\nPress Enter to exit.")
