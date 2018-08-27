from itertools import combinations

from scipy.special import comb

from Cards import Cards
from Game import Game
from Player import Player
from Table import Table

hero = Player(name="Hero", positionAtTable=0, stack=1000)
villain = Player(name="Villain", positionAtTable=1, stack=1000)
table = Table(players=[hero, villain], bigBlind=100)
