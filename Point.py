from Enums import Ranking


class Point:

    def __init__(self, ranking, kickers):
        self.ranking = ranking
        self.kickers = kickers  # Sorting is made on FullHand creation, so no need here

    def __str__(self):
        description = str(self.ranking.name)

        if self.ranking in [Ranking.POKER, Ranking.FULL_HOUSE, Ranking.THREE_OF_A_KIND, Ranking.TWO_PAIR]:
            description += " of " + str(self.kickers[0])
            if self.ranking == Ranking.FULL_HOUSE:
                description += " and " + str(self.kickers[3])
            elif self.ranking == Ranking.TWO_PAIR:
                description += " and " + str(self.kickers[2])
        else:
            description += " at " + str(self.kickers[0])

        return description

    def __hash__(self):
        return self.ranking.value + hash(tuple(self.kickers))

    def __eq__(self, other):
        return self.ranking == other.ranking and self.kickers == other.kickers

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.ranking < other.ranking:
            return True
        for i in range(len(self.kickers)):
            if self.kickers[i] < other.kickers[i]:
                return True
        return False
