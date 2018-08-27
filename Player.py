from itertools import combinations

from scipy.special import comb

from Cards import FullHand, Cards
from Exceptions import StackIsLessThanBigBlind, StackIsLessThanSmallBlind, PlayerIsNotInAGameException


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
        if self.stack < self.table.bigBlind / 2:
            self.currentBet = self.stack
            self.stack = 0
            raise StackIsLessThanSmallBlind
        else:
            self.stack -= self.table.bigBlind / 2
            self.currentBet = self.table.bigBlind / 2

    def getBestFiveCards(self):
        cards = Cards(*(list(self.hand) + self.table.board))
        fhs = [None]*comb(len(cards), 5, exact=True, repetition=False)
        for i, c in enumerate(combinations(cards, 5)):
            fhs[i] = FullHand(*c)
        return sorted(fhs, key=lambda x: x.point, reverse=True)[0]

    def setHand(self, *cards):
        if self.game is None:
            raise PlayerIsNotInAGameException
        self.hand = Cards(*cards)
        for card in cards:
            self.game.deck.remove(card)

    def setHandIgnoringDiscard(self, *cards):
        if self.game is None:
            raise PlayerIsNotInAGameException
        self.hand = Cards(*cards)

    def play(self):
        if not self.isActive:
            pass
        self.hasSpoken = True
        self.fold()
        pass  # TODO

    def fold(self):
        self.isActive = False
        print("{} has folded.".format(self))

    def isReadyToProceedToNextRound(self):
        return self.hasSpoken and ((not self.isActive) or self.currentBet == self.game.maxBet or self.stack == 0)

    def __str__(self):
        if self.name != "":
            representation = self.name
        else:
            representation = "Player #" + str(self.positionAtTable + 1)
        if self.hand is not None:
            representation += " - " + str(Cards(*self.hand))
        return representation
