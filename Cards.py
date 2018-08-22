from collections import Counter
from statistics import mode, StatisticsError

from Enums import Rank, Ranking, Suit
from Exceptions import NotFullHandException, DuplicateCardInFullHandInputException, NoPointException
from Point import Point


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + str(self.suit.symbol)

    def __hash__(self):
        return 13 * self.suit.order + self.rank.value - 1

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


class Cards(list):
    def __init__(self, *cards):
        super().__init__(cards)

    def __str__(self):
        return " ".join(map(lambda x: str(x), self))


class Deck(Cards):
    def __init__(self):
        super().__init__()
        for suit in Suit:
            for rank in Rank:
                self.append(Card(suit, rank))


class FullHand(Cards):
    def __init__(self, *cards):
        super().__init__(*cards)

        if len(self) != 5:
            if len(cards) != 5:
                raise NotFullHandException
            else:
                raise DuplicateCardInFullHandInputException

        self.suits = set(map(lambda x: x.suit, self))
        self.ranks = sorted(list(map(lambda x: x.rank, self)))
        self.maxRank = max(self.ranks)
        self.allSameSuit = (len(self.suits) == 1)
        self.numberOfDifferentRanks = len(set(self.ranks))
        if self.ranks[4] == self.ranks[0] + 4:
            self.straight = True
        elif self.maxRank == Rank.A:
            self.straight = self.ranks[3] == self.ranks[0] + 3 and (self.ranks[3] == Rank.K or self.ranks[0] == Rank.TWO)
        else:
            self.straight = False

        try:
            self.rankMode = mode(self.ranks)
            self.rankModeOccurrence = self.ranks.count(self.rankMode)
            self.kickers = [self.rankMode] * self.rankModeOccurrence
            self.kickers.extend([x for x in self.ranks if x != self.rankMode])
        except StatisticsError:
            ranksSet = set(self.ranks)
            if len(ranksSet) == 3:  # Necessarily TWO_PAIRS
                counter = Counter(self.ranks)
                pair1, pair2, kicker = counter.most_common()
                pair1, pair2 = sorted([pair1[0], pair2[0]], reverse=True)
                kicker = kicker[0]
                self.kickers = [pair1, pair1, pair2, pair2, kicker]
                self.rankMode = self.kickers[0]
                self.rankModeOccurrence = 2
                self.point = Point(Ranking.TWO_PAIR, self.kickers)
                return
            else:
                self.rankMode = self.ranks[0]
                self.rankModeOccurrence = 1
                self.kickers = self.ranks[::-1]     # Clever way to obtain a copy of a list with reversed order (not an iterator!)

        if self.straight and self.allSameSuit:
            self.point = Point(Ranking.STRAIGHT_FLUSH, self.kickers)

        elif self.numberOfDifferentRanks == 2:
            if self.rankModeOccurrence == 4:
                self.point = Point(Ranking.POKER, self.kickers)
            else:
                self.point = Point(Ranking.FULL_HOUSE, self.kickers)

        elif self.allSameSuit:
            self.point = Point(Ranking.FLUSH, self.kickers)

        elif self.straight:
            self.point = Point(Ranking.STRAIGHT, self.kickers)

        elif self.numberOfDifferentRanks == 3:
            if self.rankModeOccurrence == 3:
                self.point = Point(Ranking.THREE_OF_A_KIND, self.kickers)
            # TWO_PAIRS is a special case, treated in try-except block above

        elif self.rankModeOccurrence == 2:
            self.point = Point(Ranking.PAIR, self.kickers)

        elif self.numberOfDifferentRanks == 5:
            self.point = Point(Ranking.HIGH_CARD, self.kickers)

        else:
            raise NoPointException
