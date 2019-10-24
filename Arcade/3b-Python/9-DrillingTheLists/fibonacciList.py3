# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/S7EJzXk7idpB2jHhy/
# XXX
def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda x, n: x + [ x[-1] + x[-2] ], range(n - 2), [0, 1])]