from collections import defaultdict
from itertools import groupby


def YACHT(dice):
    it = iter(dice)
    value = next(it)
    return 50 if all(map(lambda x: x == value, it)) else 0


sumfilter = lambda dice, num: sum(filter(lambda x: x == num, dice))
ONES = lambda x: sumfilter(x, 1)
TWOS = lambda x: sumfilter(x, 2)
THREES = lambda x: sumfilter(x, 3)
FOURS = lambda x: sumfilter(x, 4)
FIVES = lambda x: sumfilter(x, 5)
SIXES = lambda x: sumfilter(x, 6)


def FULL_HOUSE(dice):
    values = set(dice)
    freq = dice.count(next(iter(values)))
    return sum(dice) if len(values) == 2 and freq in (2, 3) else 0


def FOUR_OF_A_KIND(dice):
    matches = defaultdict(list)
    for k, g in groupby(dice):
        matches[k].extend(list(g))
        if len(matches[k]) >= 4:
            return 4 * k
    else:
        return 0


LITTLE_STRAIGHT = lambda dice: straight(dice, 5)
BIG_STRAIGHT = lambda dice: straight(dice, 6)


def straight(dice, high_value):
    while dice:
        try:
            dice.remove(high_value)
        except ValueError:
            return 0
        else:
            high_value -= 1
    return 30


CHOICE = sum


def score(dice, category):
    return category(dice)
