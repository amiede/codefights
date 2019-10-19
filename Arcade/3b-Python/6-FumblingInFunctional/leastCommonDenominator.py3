# https://app.codesignal.com/arcade/python-arcade/fumbling-in-functional/cYG6vtfv6TJKPsvSY/
from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda x, y: x * y // gcd(x, y), denominators)