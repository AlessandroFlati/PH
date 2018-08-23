from Exceptions import StackIsLessThanBigBlind, StackIsLessThanSmallBlind


class Player:

    def __init__(self, name="", positionAtTable=0, stack=0):
        self.name = name
        self.stack = stack
        self.currentBet = 0
        self.isActive = True
        self.isAllIn = False
        self.hand = None
        self.table = None
        self.positionAtTable = positionAtTable
        self.game = None
        self.hasSpoken = False

    def nextToSpeak(self):
        return self.table.players[(self.positionAtTable + 1) % self.table.size]

    def putBigBlind(self):
        if self.stack < self.table.bigBlind:
            self.currentBet = self.stack
            self.stack = 0
            raise StackIsLessThanBigBlind
        else:
            self.stack -= self.table.bigBlind
            self.currentBet = self.table.bigBlind

    def putSmallBlind(self):
        if self.stack < self.table.bigBlind/2:
            self.currentBet = self.stack
            self.stack = 0
            raise StackIsLessThanSmallBlind
        else:
            self.stack -= self.table.bigBlind/2
            self.currentBet = self.table.bigBlind/2

    def play(self):
        self.hasSpoken = True
        pass  # TODO

    def fold(self):
        self.isActive = False
        self.table.activePlayers.remove(self)

    def __str__(self):
        if self.name != "":
            representation = self.name
        else:
            representation = "Player #" + str(self.positionAtTable+1)
        representation += ": {}".format(self.hand)
        return representation
