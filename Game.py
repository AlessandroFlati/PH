import random
from time import sleep

from Board import Board
from Cards import Deck, Cards
from Enums import GameRound
from Exceptions import GameShouldHaveEndedException, IncorrectNumberOfCardsFlippedException


class Game:
    def __init__(self, table=None):
        self.winners = []
        self.alreadyShowedGameRound = False
        self.table = table
        self.deck = Deck()
        self.gameRound = GameRound.PREFLOP
        self.maxBet = 0
        self.currentPlayer = None

        for player in self.table.players:
            player.game = self
        self.table.board = Board()
        self.table.board.game = self

    def __str__(self):
        representation = ""
        if not self.alreadyShowedGameRound:
            if self.gameRound != GameRound.PREFLOP:
                representation += "\n\n"
            representation += "Game Round: {}\n\n".format(self.gameRound.name)

        if self.gameRound != GameRound.END:
            representation += "Player playing: {}\n\n{}\n".format(self.currentPlayer, self.table)
        else:
            representation += "Winner: " + str(self.winners)
        return representation

    def handleGameRound(self):
        self.currentPlayer = self.table.firstToSpeak()
        if self.gameRound == GameRound.PREFLOP:
            self.handlePreFlop()
        elif self.gameRound == GameRound.FLOP:
            self.handleFlop()
        elif self.gameRound == GameRound.TURN:
            self.handleTurn()
        elif self.gameRound == GameRound.RIVER:
            self.handleRiver()
        elif self.gameRound == GameRound.END:
            bestFiveCards = {player: player.getBestFiveCards() for player in self.table.players}
            ranking = sorted(bestFiveCards, key=lambda x: bestFiveCards[x].point, reverse=True)
            bestPoint = bestFiveCards[ranking[0]].point
            self.winners.extend(filter(lambda x: bestFiveCards[x].point == bestPoint, ranking))

            # handle winners, tiers and losers money
            return self.winners
        else:
            raise GameShouldHaveEndedException

        # print(self)

        self.handleGameRound()

    def handlePreFlop(self):
        if self.maxBet == 0:
            self.table.handleSmallBlind()
            self.table.handleBigBlind()
            self.maxBet = self.table.bigBlind
            # for player in self.table.players:
            #     player.cards = Cards(*self.getRandomCardsFromDeck(2))
        self.currentPlayer.play()
        self.advanceInGame()

    def handleFlop(self):
        if self.maxBet == 0:
            self.table.board[0], self.table.board[1], self.table.board[2] = self.getRandomCardsFromDeck(3)
        self.currentPlayer.play()
        self.advanceInGame()

    def handleTurn(self):
        if self.maxBet == 0:
            self.table.board[3] = self.getRandomCardsFromDeck(1)[0]
        self.currentPlayer.play()
        self.advanceInGame()

    def handleRiver(self):
        if self.maxBet == 0:
            self.table.board[4] = self.getRandomCardsFromDeck(1)[0]
        self.currentPlayer.play()
        self.advanceInGame()

    def prepareForNextRound(self):
        for player in self.table.players:
            player.hasSpoken = False
            player.currentBet = 0
        self.alreadyShowedGameRound = False

    def advanceInGame(self):
        if len(list(filter(lambda x: not x.isActive, self.table.players))) == 1:
            self.gameRound = GameRound.END
            self.prepareForNextRound()
        if all(map(lambda x: x.isReadyToProceedToNextRound(), self.table.players)):
            self.gameRound = GameRound(self.gameRound + 1)
            self.prepareForNextRound()
            self.currentPlayer = self.table.firstToSpeak()
        else:
            self.currentPlayer = self.currentPlayer.nextToSpeak()

    def getRandomCardsFromDeck(self, numberOfCards):
        return [self.deck.pop(random.randrange(len(self.deck))) for _ in range(numberOfCards)]

    def updateGameRound(self):
        if any(map(lambda x: x.hand is None, self.table.players)):
            self.gameRound = GameRound.PREFLOP
        numberOfCardsFlipped = len(list(filter(lambda x: x is not None, self.table.board)))
        if numberOfCardsFlipped == 0:
            self.gameRound = GameRound.FLOP
        elif numberOfCardsFlipped == 3:
            self.gameRound = GameRound.TURN
        elif numberOfCardsFlipped == 4:
            self.gameRound = GameRound.RIVER
        elif numberOfCardsFlipped == 5:
            self.gameRound = GameRound.END
        else:
            raise IncorrectNumberOfCardsFlippedException
