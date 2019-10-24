# https://app.codesignal.com/arcade/python-arcade/showing-class/q8K5YLLNvvQ2fahiB/
class Counter(object):
    def __init__(self, beta): self.value = beta

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()
