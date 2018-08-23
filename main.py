from Board import Board
from Cards import Card, Cards
from Enums import Suit, Rank
from Player import Player
from Table import Table

board = Board(Card(Suit.CLUBS, Rank.A), Card(Suit.DIAMONDS, Rank.A), Card(Suit.CLUBS, Rank.Q), Card(Suit.DIAMONDS, Rank.J), Card(Suit.HEARTS, Rank.K))
heroHand = Cards(Card(Suit.SPADES, Rank.A), Card(Suit.SPADES, Rank.K))
villainHand = Cards(Card(Suit.HEARTS, Rank.A), Card(Suit.HEARTS, Rank.Q))
hero = Player(name="Hero", positionAtTable=0, stack=1000)
villain = Player(name="Villain", positionAtTable=1, stack=1000)
table = Table(board=board, players=[hero, villain])

print(hero)
print(villain)
print(table)
