from Enums import GameRound
from Exceptions import GameShouldHaveEndedException


class Game:
    def __init__(self, table=None):
        self.gameRound = GameRound.PREFLOP
        self.maxBet = 0
        self.table = table
        for player in self.table.players:
            player.game = self
        self.currentPlayer = self.table.firstToSpeak()

    def __str__(self):
        representation = "Turn: {}\n\n{}".format(self.gameRound, self.table)
        return representation

    def handleGameRound(self):
        if self.gameRound == GameRound.PREFLOP:
            self.handlePreFlop()
        elif self.gameRound == GameRound.FLOP:
            self.handleFlop()
        elif self.gameRound == GameRound.TURN:
            self.handleTurn()
        elif self.gameRound == GameRound.RIVER:
            self.handleRiver()
        elif self.gameRound == GameRound.END:

            for player in self.table.players:
                player.game = None
            return  # TODO?
        else:
            raise GameShouldHaveEndedException

        self.handleGameRound()

    def handlePreFlop(self):
        if self.maxBet == 0:
            self.table.handleSmallBlind()
            self.table.handleBigBlind()
            self.maxBet = self.table.bigBlind
        self.currentPlayer.play()
        self.advanceInGame()

    def handleFlop(self):
        # TODO
        self.currentPlayer.play()
        self.advanceInGame()

    def handleTurn(self):
        # TODO
        self.currentPlayer.play()
        self.advanceInGame()

    def handleRiver(self):
        # TODO
        self.currentPlayer.play()
        self.advanceInGame()

    def advanceInGame(self):
        if all(map(lambda x: ((not x.isActive) or x.currentBet == self.maxBet or x.stack == 0) and x.hasSpoken, self.table.players)):
            self.gameRound = GameRound(self.gameRound + 1)
            for player in self.table.players:
                player.hasSpoken = False
                player.currentBet = 0
            self.currentPlayer = self.table.firstToSpeak()
        else:
            self.currentPlayer = self.currentPlayer.nextToSpeak()
