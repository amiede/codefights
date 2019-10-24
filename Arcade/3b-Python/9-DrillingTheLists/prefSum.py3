# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/Enwr8TBeTbuFbuPzu/
# XXX
def prefSum(a):
    return functools.reduce(lambda x, y: x + [ x[-1] + y ], a, [0])[1:]