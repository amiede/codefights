# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/TCTvJoBJq9wBLLJ64
def mathPractice(numbers):
    return functools.reduce(lambda a, b: a + b[1] if b[0] % 2 else a * b[1], enumerate(numbers), 1)