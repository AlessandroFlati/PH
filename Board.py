from Cards import Cards


class Board(list):
    def __init__(self, *cards):
        super().__init__(cards)
        self.extend([None] * (5 - len(self)))

    def getFlop(self):
        return Cards(*self[:3])

    def getTurn(self):
        return self[3]

    def getRiver(self):
        return self[4]

    def isFull(self):
        return None in self

    def __str__(self):
        return "| " + " | ".join([str(Cards(*self[:3])), str(self[3]), str(self[4])]) + " |"

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)
