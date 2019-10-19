# https://app.codesignal.com/arcade/python-arcade/itertools-kit/opua5BqfJSaW9ny4Q
# https://docs.python.org/3/library/itertools.html#itertools.permutations
from itertools import permutations

def kthPermutation(numbers, k):
    return sorted(permutations(numbers))[k-1]