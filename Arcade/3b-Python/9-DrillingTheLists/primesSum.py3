# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/K5fiXbgF26gdt8uJT/
# XXX
def primesSum(a, b):
    return sum(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(max(2, a), b+1)))