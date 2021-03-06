class NotFullHandException(NameError):
    pass


class DuplicateCardInFullHandInputException(NameError):
    pass


class NoPointException(NameError):
    pass


class GameEndedException(NameError):
    pass


class StackIsLessThanBigBlind(NameError):
    pass


class StackIsLessThanSmallBlind(NameError):
    pass


class GameShouldHaveEndedException(NameError):
    pass


class PlayerIsNotInAGameException(NameError):
    pass


class BoardIsNotInAGameException(NameError):
    pass


class IncorrectNumberOfCardsFlippedException(NameError):
    pass
