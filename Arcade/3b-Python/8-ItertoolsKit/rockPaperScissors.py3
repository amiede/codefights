# https://app.codesignal.com/arcade/python-arcade/itertools-kit/d9Ru2ARE5tXoQ9KgR
# https://docs.python.org/3/library/itertools.html#itertools.permutations
from itertools import permutations

def rockPaperScissors(players):
    return sorted(list(permutations(players,2)))