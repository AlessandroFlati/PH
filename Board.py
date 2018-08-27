from Cards import Cards
from Exceptions import BoardIsNotInAGameException


class Board(list):
    def __init__(self, *cards):
        super().__init__(cards)
        self.extend([None] * (5 - len(self)))
        self.game = None

    def getFlop(self):
        return Cards(*self[:3])

    def getTurn(self):
        return self[3]

    def getRiver(self):
        return self[4]

    def isFull(self):
        return not (None in self)

    def setCards(self, *cards):
        if self.game is None:
            raise BoardIsNotInAGameException
        self[0:len(cards)] = cards
        for card in cards:
            self.game.deck.remove(card)

    def setCardsIgnoringDiscard(self, *cards):
        if self.game is None:
            raise BoardIsNotInAGameException
        self[0:len(cards)] = cards

    def __str__(self):
        representation = "| "
        if None in self.getFlop():
            representation += "      |   |   |"
        else:
            representation += str(self.getFlop()) + " | "
            if self[3] is None:
                representation += "  |   |"
            else:
                representation += str(self[3]) + " | "
                if self[4] is None:
                    representation += "  |"
                else:
                    representation += str(self[4]) + " |"
        return representation

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)
