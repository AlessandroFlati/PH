from enum import Enum, IntEnum


class Ranking(IntEnum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    POKER = 8
    STRAIGHT_FLUSH = 9


class Rank(IntEnum):
    A = 14
    K = 13
    Q = 12
    J = 11
    T = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

    def getRankFromImage(self, image):
        pass

    def __str__(self):
        if self.value < 10:
            return str(self.value)
        else:
            return self.name


class Suit(Enum):
    SPADES = ("♠", 0)
    HEARTS = ("♥", 1)
    DIAMONDS = ("♦", 2)
    CLUBS = ("♣", 3)

    def __init__(self, symbol, order):
        self.symbol = symbol
        self.order = order

    def __str__(self):
        return self.symbol


class Turn(IntEnum):
    PREFLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    END = 4

    def __str__(self):
        return self.name


class PixelPosition(Enum):  # X, Y, WIDTH, HEIGHT
    FirstCardRank = (1030, 737, 36, 45)
    FirstCardRankLeft = (752, 737, 36, 45)
    FirstCardSuit = (1030, 782, 34, 34)
    FirstCardSuitLeft = (751, 782, 34, 34)
    SecondCardRank = (1030 + 44, 737 + 9, 36, 45)
    SecondCardRankLeft = (752 + 44, 737 + 9, 36, 45)
    SecondCardSuit = (1030 + 44, 782 + 9, 34, 34)
    SecondCardSuitLeft = (751 + 44, 782 + 9, 34, 34)
    Board = (622, 432, 676, 181)
    BoardFirstCard = (0, 0, 128, 181)
    BoardSecondCard = (137, 0, 128, 181)
    BoardThirdCard = (274, 0, 128, 181)
    BoardFourthCard = (411, 0, 128, 181)
    BoardFifthCard = (548, 0, 128, 181)
    Rank = (29, 10, 72, 72)
    Suit = (29, 95, 72, 72)
    Pot = (622, 350, 676, 27)
    Blinds = (672, 682, 576, 30)
    SixPlayers1 = (371, 653, 1, 1)  # 255 255 255
    SixPlayers2 = (371, 256, 1, 1)
    SixPlayers3 = (981, 153, 1, 1)
    SixPlayers4 = (1606, 255, 1, 1)
    SixPlayers5 = (1606, 652, 1, 1)
    SixPlayers1CurrentBet = (507, 636, 111, 25)
    SixPlayers2CurrentBet = (507, 406, 111, 25)
    SixPlayers3CurrentBet = (1152, 292, 111, 25)
    SixPlayers4CurrentBet = (1295, 406, 111, 25)
    SixPlayers5CurrentBet = (1295, 636, 111, 25)
    SixPlayers1Stack = (280, 746, 233, 29)
    SixPlayers2Stack = (280, 344, 233, 29)
    SixPlayers3Stack = (898, 238, 233, 29)
    SixPlayers4Stack = (1408, 344, 233, 29)
    SixPlayers5Stack = (1408, 746, 233, 29)
    NinePlayers1 = (485, 721, 1, 1)
    NinePlayers1CurrentBet = (575, 704, 111, 25)
    NinePlayers1Stack = (349, 808, 233, 29)
    NinePlayers2 = (277, 538, 1, 1)
    NinePlayers2CurrentBet = (491, 622, 111, 25)
    NinePlayers2Stack = (209, 631, 233, 29)
    NinePlayers3 = (277, 351, 1, 1)
    NinePlayers3CurrentBet = (491, 416, 111, 25)
    NinePlayers3Stack = (209, 444, 233, 29)
    NinePlayers4 = (638, 164, 1, 1)
    NinePlayers4CurrentBet = (713, 315, 111, 25)
    NinePlayers4Stack = (554, 252, 233, 29)
    NinePlayers5 = (1335, 164, 1, 1)
    NinePlayers5CurrentBet = (1076, 315, 111, 25)
    NinePlayers5Stack = (1134, 252, 233, 29)
    NinePlayers6 = (1686, 351, 1, 1)
    NinePlayers6CurrentBet = (1298, 416, 111, 25)
    NinePlayers6Stack = (1478, 444, 233, 29)
    NinePlayers7 = (1686, 538, 1, 1)
    NinePlayers7CurrentBet = (1298, 622, 111, 25)
    NinePlayers7Stack = (1478, 631, 233, 29)
    NinePlayers8 = (1468, 721, 1, 1)
    NinePlayers8CurrentBet = (1215, 704, 111, 25)
    NinePlayers8Stack = (1339, 808, 233, 29)

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
