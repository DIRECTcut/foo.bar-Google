"""Foo.Bar Chapter 2 Solution"""

from functools import reduce
from timer import time_function


def is_odd(j):
    """Returns True if passed an odd integer, otherwise returns False"""
    if j % 2 == 0:
        return False

    return True


def multiply(j):
    """Returns the product of all integers in the list, excluding zeroes."""
    j = list(filter(lambda x: x != 0, j))

    return int(reduce(lambda a, b: a * b, j))


@time_function
def solution(xs):
    """Solution function"""
    lists_with_one_excluded = [xs[0:x] + xs[x + 1 :] for x in range(len(xs))]
    products = [multiply(l) for l in lists_with_one_excluded]

    return str(max(products))
