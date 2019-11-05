from blackjack_simulator.card import Card


class Deck(set):
    """Base object for representing deck of cards.

    Inherited from set object, but initializated with
    """

    def __init__(self):
        super().__init__([
            Card(value, suit)
            for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
            for suit in Card.AVAILABLE_SUITS
        ])

    def draw(self):
        return super().pop()

    def shuffle(self):
        """Reset deck."""
        self.update(Deck())
