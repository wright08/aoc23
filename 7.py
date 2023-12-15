from io import StringIO
from functools import cmp_to_key

ex = StringIO("""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""")

def getHandType(cards):
    if len(cards) == 1: return 7 # five of kind
    if 4 in cards.values(): return 6 # four of a kind
    if len(cards) == 2: return 5 # full House
    if 3 in cards.values(): return 4 # three of a kind
    if pairs := len([count for count in cards.values() if count == 2]):
        if pairs == 2: return 3 # two pair
        return 2 # pair
    return 1 # high card

def part_1():
    with open('inputs/7') as f:
        lines = f.read().splitlines()

    def cmp(a, b):
        if d := getHandType(a[0]) - getHandType(b[0]):
            return d
        camelCards = 'AKQJT98765432'
        for a, b in zip(a[2], b[2]):
            if d := camelCards.index(b) - camelCards.index(a):
                return d
        return 0

    allHandsBids = []
    for hand in lines:
        hand, bid = hand.split()
        cardsD = {}
        for card in hand:
            cardsD[card] = cardsD.setdefault(card, 0) + 1
        allHandsBids.append((cardsD, int(bid), hand))

    winnings = sum([rank * hand[1] for rank, hand in enumerate(sorted(allHandsBids, key=cmp_to_key(cmp)), start=1)])
    print(winnings)

def part_2():
    with open('inputs/7') as f:
        lines = f.read().splitlines()
    
    def cmp(a, b):
        if d := getHandType(a[0]) - getHandType(b[0]):
            return d
        camelCards = 'AKQT98765432J'
        for a, b in zip(a[2], b[2]):
            if d := camelCards.index(b) - camelCards.index(a):
                return d
        return 0

    allHandsBids = []
    for hand in lines:
        hand, bid = hand.split()
        cardsD = {}
        for card in hand:
            cardsD[card] = cardsD.setdefault(card, 0) + 1
        allHandsBids.append((cardsD, int(bid), hand))
        if jokers := cardsD.get('J'):
            if jokers < 5:
                del cardsD['J']
            maxPile = max(cardsD.items(), key=lambda x: x[1])[0]
            cardsD[maxPile] += jokers 

    winnings = sum([rank * hand[1] for rank, hand in enumerate(sorted(allHandsBids, key=cmp_to_key(cmp)), start=1)])
    print(winnings)

part_1()
part_2()