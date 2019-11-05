from collections.abc import Iterable

from blackjack_simulator.utils import raise_close_match_error

AS_VALUE = set([1, 11])


def str2value(string):
    """Convert string representation of card to numerical value."""
    string = string.lower()
    exception = 'Should be number between 1 and 10, "j", "q", "k" or "a"'
    try:
        value = int(string)
        if value == 1:
            return AS_VALUE
        elif not 2 <= value <= 10:
            raise ValueError(exception)
    except ValueError:
        if string in ['j', 'q', 'k']:
            return 10
        elif string == 'a':
            return AS_VALUE
        else:
            raise ValueError(exception)


def value2str(string):
    """Convert numerical value of card to string."""
    string = string.lower()
    exception = 'Should be number between 1 and 10, "j", "q", "k" or "a"'
    try:
        value = int(string)
        if value == 1:
            return AS_VALUE
        elif not 2 <= value <= 10:
            raise ValueError(exception)
    except ValueError:
        if string in ['j', 'q', 'k']:
            return 10
        elif string == 'a':
            return AS_VALUE
        else:
            raise ValueError(exception)


class Card:

    AVAILABLE_SUITS = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self, value, suit):
        if isinstance(value, str):
            value = strtovalue(value)
            string = value.upper()
        elif value == 1:
            value = AS_VALUE
            string = 'A'
        else:
            string = str(value)
        self._value = value
        self._string = string
        self.suit = raise_close_match_error(suit, self.AVAILABLE_SUITS, 'suit')

    def __str__(self):
        return self._string

    def __int__(self):
        try:
            return int(self._value)
        except TypeError:
            return 1

    def __add__(self, other):
        if isinstance(self._value, Iterable):
            if isinstance(other.value, Iterable):
                return set([a + b for a in self._value for b in other.value])
            else:
                return set([a + other.value for a in self._value])
        else:
            if isinstance(other.value, Iterable):
                return set([a + self._value for a in other.value])
            else:
                return other.value + self._value

    def __hash__(self):
        """Define hash funcion for correct definition of unique properties.

        The hash function value used will be the position in the ordered deck,
        being the order of the suits the one defined in Card.AVAILABLE_SUITS.
        """
        integer = int(self)
        if 1 <= integer < 10:
            position = integer
        else:
            position = 11 + ['J', 'Q', 'K'].index(str(self))
        return self.AVAILABLE_SUITS.index(self.suit) * 13 + position
