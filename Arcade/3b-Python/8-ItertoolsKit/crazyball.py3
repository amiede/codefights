# https://app.codesignal.com/arcade/python-arcade/itertools-kit/nPt9LX3Piip9ZspLv
# https://docs.python.org/3/library/itertools.html#itertools.combinations
from itertools import combinations

def crazyball(players, k):
    return list(combinations(sorted(players),k))
