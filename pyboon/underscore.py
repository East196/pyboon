
from functools import reduce


def map2(items, func):
    items = map(func, items)
    return list(items)


def filter2(items, func):
    items = filter(func, items)
    return list(items)


def reduce2(items, func):
    return reduce(func, items)


def size(into):
    return len(into)
