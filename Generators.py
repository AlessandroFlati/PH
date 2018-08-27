from itertools import combinations
from multiprocessing import Lock, Process, Array, Value
from time import time

from scipy.special import comb

from Cards import Cards, Deck, FullHand
from Enums import GameRound
from Player import Player
from Table import Table

showdownCombinations = combinations(Deck(), 9)
numberOfCombinations = comb(52, 9, exact=True, repetition=False)
chunks = []
chunkSize = 100


def generateAllFullHands(verbose=False):
    previousPercentage = 0.
    deck = Deck()
    fhs = [0] * 2598960
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


def toChunks(lock, s):
    global chunks
    chunks.append(s)
    if len(chunks) == chunkSize:
        lock.acquire()
        with open('CSV/Showdowns.csv', 'a+', encoding='utf-8') as sd:
            sd.write('\n'.join(chunks))
        lock.release()
        chunks = []


def generateAllShowdownsFor2Players(lock, counter, previousPercentage, initial_time, verbose=True):
    hero = Player(name="Hero", positionAtTable=0, stack=1000)
    villain = Player(name="Villain", positionAtTable=1, stack=1000)
    table = Table(players=[hero, villain], bigBlind=100)
    table.game.gameRound = GameRound.END
    # probabilities = {heroHand: {villainHand: {board: 0 for board in combinations(table.game.deck, 5)} for villainHand in combinations(table.game.deck, 2)} for heroHand in combinations(table.game.deck, 2)}
    # probabilities = {}

    while counter.value < numberOfCombinations:
        cards = next(showdownCombinations)  # TODO - HOW TO PROCESS LOCK? CHECK POINTS!
        counter.value += 1

        hero.setHandIgnoringDiscard(*cards[:2])
        villain.setHandIgnoringDiscard(*(cards[2:4]))
        table.board.setCardsIgnoringDiscard(*(cards[4:9]))

        heroPoint = hero.getBestFiveCards().point
        villainPoint = hero.getBestFiveCards().point
        if heroPoint == villainPoint:
            win, tie, lose = 0, 1, 0
        elif heroPoint > villainPoint:
            win, tie, lose = 1, 0, 0
        else:
            win, tie, lose = 0, 0, 1

        toChunks(lock, '{};{};{};{};{};{}'.format(str(hero.hand), str(villain.hand), Cards(*table.board), win, tie, lose))

        # if hero.hand not in probabilities:
        #     probabilities[hero.hand] = {}
        # if villain.hand not in probabilities[hero.hand]:
        #     probabilities[hero.hand][villain.hand] = {}
        # if board not in probabilities[hero.hand][villain.hand]:
        #     probabilities[hero.hand][villain.hand][board] = 0

        if verbose:
            percentage = round(counter.value / numberOfCombinations, 6)
            # if percentage > previousPercentage.value:
            #     previousPercentage.value = percentage
            #     print("{:.2f} - {:.4f}%".format(time() - initial_time.value, percentage * 100))
            if percentage >= 0.00001:  # EXIT
                lock.acquire()
                with open('CSV/Showdowns.csv', 'a+', encoding='utf-8') as sd:
                    sd.write('\n')
                    sd.write('\n'.join(chunks))
                lock.release()
                return

    lock.acquire()
    with open('CSV/Showdowns.csv', 'a+', encoding='utf-8') as f:
        f.write('\n'.join(chunks))
    lock.release()


if __name__ == '__main__':
    with open('CSV/Showdowns.csv', 'w', encoding='utf-8') as f:
        f.write('heroHand;villainHand;board;win;tie;lose\n')  # Header

    processLock = Lock()
    cntr = Value('f', 0)
    pp = Value('f', 0)
    t0 = Value('d', time())
    processes = []
    for i in range(17):
        process = Process(target=generateAllShowdownsFor2Players, args=(processLock, cntr, pp, t0))
        processes.append(process)
        process.start()
    [thread.join() for thread in processes]

    print(cntr.value)
    with open('CSV/Showdowns.csv', 'r', encoding='utf-8') as f:
        for n, l in enumerate(f):
            pass
    print(n + 1)

    print(time() - t0.value)
