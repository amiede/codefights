# https://app.codesignal.com/arcade/python-arcade/complexity-of-comprehension/a6DD4JaT2moH22XTf/description
def coolPairs(a, b):
    uniqueSums = {i + j for i in a for j in b if (i * j) % (i + j) == 0}
    return len(uniqueSums)