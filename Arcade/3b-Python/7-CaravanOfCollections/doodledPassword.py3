# https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/aarR4B273h5D2x8ry/
# https://pymotw.com/2/collections/deque.html
from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x,y: x.rotate(-y), res, range(n)), 0)
    return [list(d) for d in res]