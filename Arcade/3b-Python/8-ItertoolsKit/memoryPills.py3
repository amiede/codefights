# https://app.codesignal.com/arcade/python-arcade/itertools-kit/R2GeRWE2SXz4eLAe5/
# https://docs.python.org/3/library/itertools.html
from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda x: len(x) % 2 != 0, pills + [""] * 3 )
    next(gen)
    return [next(gen) for _ in range(3)]