# https://app.codesignal.com/arcade/python-arcade/itertools-kit/k2MEPqLJn5YEWafkt
# https://docs.python.org/3/library/itertools.html#itertools.product
from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [ i for i in sorted(map(createNumber, product(digits, repeat=k))) if int(i) % d == 0 ]
