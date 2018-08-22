from itertools import combinations

from Cards import Deck, FullHand


def generateAllFullHands(verbose=False):
    previousPercentage = 0.
    deck = Deck()
    fhs = [0]*2598960
    for i, cards in enumerate(combinations(deck, 5)):
        fhs[i] = FullHand(*cards)
        if verbose:
            percentage = round(i / 2598960, 3)
            if percentage > previousPercentage:
                previousPercentage = percentage
                print("{:.1f}%".format(percentage * 100))
    return fhs


def generateAllPoints(verbose=False):
    return set(map(lambda x: x.point, generateAllFullHands(verbose)))
