from blackjack_simulator.exceptions import NoMoreBudget


class Player:
    def __init__(self, budget, strategy):
        self.budget = budget
        self.strategy = strategy

    def bet(self, amount):
        self.budget -= amount
        if self.budget < 0:
            raise NoMoreBudget('You are out of budget and cannot do this bet.')

    def play(self, hand, game):
        value = self.strategy.play(hand, self, game)
        return value
