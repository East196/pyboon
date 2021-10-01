
from functools import reduce


def map2(items, func):
    items = map(func, items)
    return list(items)


def filter2(items, func):
    items = filter(func, items)
    return list(items)


def find(items, func):
    items = filter(func, items)
    items = list(items)
    return items[0] if items else None


def reduce2(items, func):
    return reduce(func, items)


def range2(*into):
    if isinstance(into, list) or isinstance(into, tuple):
        return list(range(*into))
    return list(range(into))


def size(into):
    return len(into)


def trim(s):
    return s.strip()


def repeat(s, n=2):
    return s*n


def pad(s, n=0, c='0'):
    if n <= len(s):
        return s
    return c*(n-len(s))+s
