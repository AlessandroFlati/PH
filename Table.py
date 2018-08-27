from itertools import cycle

from Board import Board
from Enums import GameRound
from Game import Game


class Table:
    def __init__(self, board=Board(), players=None, dealerPosition=0, ante=0, bigBlind=0):
        self.board = board
        self.ante = ante
        self.bigBlind = bigBlind
        self.players = sorted(players, key=lambda x: x.positionAtTable)
        self.size = len(self.players)
        for player in self.players:
            player.table = self
        self.dealerPosition = dealerPosition
        self.dealer = self.players[self.dealerPosition]
        self.game = Game(table=self)

    def __str__(self):
        representation = str(self.board)
        return representation

    def advanceDealer(self):
        self.dealerPosition = (self.dealerPosition + 1) % self.size
        self.dealer = self.players[self.dealerPosition]

    def handleNewGame(self):
        self.advanceDealer()
        for player in self.players:
            player.game = None
            player.cards = None
        self.board = Board()
        self.game = Game(table=self)

    def firstToSpeak(self):
        if self.game.gameRound == GameRound.PREFLOP:
            return self.players[(self.dealerPosition + 3) % self.size]
        else:
            for i in range(self.size):
                player = self.players[(self.dealerPosition + i) % self.size]
                if player.isActive:
                    return player

    def handleBigBlind(self):
        self.players[(self.dealerPosition + 2) % self.size].putBigBlind()

    def handleSmallBlind(self):
        self.players[(self.dealerPosition + 1) % self.size].putSmallBlind()
