class Hand:

    def __init__(self, *cards):
        self.cards = cards

    def value(self):
        return [value for value in sum(cards) if value <= 21]
