# https://app.codesignal.com/arcade/python-arcade/complexity-of-comprehension/vtDLcQWTSc5tJHL6x/description
def multiplicationTable(n):
    return [ [(x+1)*(y+1) for x in range(n)] for y in range(n)]