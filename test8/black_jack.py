# Black Jack game example

import test8.cards
import test8.card_player


def main():
    # bj_card_set = test8.cards.UsualCardSet()
    bj_deck = test8.cards.Deck()
    bj_deck.create_deck(test8.cards.UsualCardSet)
    bj_deck.shuffle()

    players = test8.card_player.ask_number("How many players play current game? Enter a number from 1 to 7: ", 1, 8)
    for player in players:
        name = input("Enter player name: ")
        player = test8.card_player.CardPlayer(name)


main()
input("\nPress Enter to exit.")
