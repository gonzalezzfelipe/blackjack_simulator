import random

from blackjack_simulator.deck import Deck


class Game:
    def __init__(self, dealer, players, amount_of_decks=6):
        self.decks = [Deck() for _ in range(amount_of_decks)]

    def draw(self):
        return random.choice(self.decks).draw()

    def shuffle(self):
        [deck.shuffle() for deck in self.decks]
