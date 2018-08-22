from Enums import Turn


class Game:
    def __init__(self, turn=Turn.Preflop, maxBet=0, pot=0, ante=0, bigBlind=0, table=None):
        self.turn = turn
        self.maxBet = maxBet
        self.pot = pot
        self.ante = ante
        self.bigBlind = bigBlind
        self.table = table

    def __str__(self):
        representation = "Turn: {}\n\n{}".format(self.turn, self.table)
        return representation
