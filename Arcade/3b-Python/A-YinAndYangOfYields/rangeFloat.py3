# https://app.codesignal.com/arcade/python-arcade/yin-and-yang/CiZrg3JEputAAoc2E/
# XXX
class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def next(self):
        if (self.step > 0 and self.i >= self.stop) \
        or (self.step < 0 and self.i <= self.stop):
            raise StopIteration
        else:
            i = self.i
            self.i += self.step
            return i


def rangeFloat(args):
    return list(FRange(*args))
