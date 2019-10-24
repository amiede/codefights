# https://app.codesignal.com/arcade/python-arcade/yin-and-yang/BqA4bDcdQQcNJgkqi
class Greeter(object):
    def __init__(self, names):
        self.cnt = 0
        self.names = names

    def __iter__(self):
        return self

    def next(self):
        if self.cnt < len(self.names):
            self.cnt += 1
            return 'Hello, {}!'.format(self.names[self.cnt - 1])
        else:
            raise StopIteration


def greetingsGenerator(team):
    return list(Greeter(team))
