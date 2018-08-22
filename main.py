from Board import Board
from Cards import Card, Cards
from Enums import Suit, Rank
from PlayerAtTable import PlayerAtTable
from Table import Table

board = Board(Card(Suit.CLUBS, Rank.A), Card(Suit.DIAMONDS, Rank.A), Card(Suit.CLUBS, Rank.Q), Card(Suit.DIAMONDS, Rank.J), Card(Suit.HEARTS, Rank.K))
heroHand = Cards(Card(Suit.SPADES, Rank.A), Card(Suit.SPADES, Rank.K))
villainHand = Cards(Card(Suit.HEARTS, Rank.A), Card(Suit.HEARTS, Rank.Q))
hero = PlayerAtTable(name="Hero", positionAtTable=0, stack=1000, hand=heroHand)
villain = PlayerAtTable(name="Villain", positionAtTable=1, stack=1000, hand=villainHand)
table = Table(board=board, players=[hero, villain])

print(hero)
print(villain)
print(table)
