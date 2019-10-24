# https://app.codesignal.com/arcade/python-arcade/yin-and-yang/KAvAhLPEzyx6dBKYT
# https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
def fibonacciGenerator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]
