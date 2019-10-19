# https://app.codesignal.com/arcade/python-arcade/itertools-kit/cDuMQ6Fd4N58zdCWN
# https://docs.python.org/3/library/itertools.html#itertools.count
# https://docs.python.org/3/library/itertools.html#itertools.takewhile
from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)