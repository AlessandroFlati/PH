class PlayerAtTable:

    def __init__(self, name="", positionAtTable=0, stack=0, currentBet=0, isActive=True, isAllIn=False, hand=None, game=None, table=None):
        self.name = name
        self.positionAtTable = positionAtTable
        self.stack = stack
        self.currentBet = currentBet
        self.isActive = isActive
        self.isAllIn = isAllIn
        self.hand = hand
        self.game = game
        self.table = table

    def __str__(self):
        if self.name != "":
            representation = self.name
        else:
            representation = "Player #" + str(self.positionAtTable)
        representation += ": {}".format(self.hand)
        return representation
