# https://codefights.com/arcade/python-arcade/complexity-of-comprehension/DfDPhgb5Bj2HQSdr5
def constructShell(n):
    return  [ [0] * (i+1) for i in range(n) ] + [ [0] * i for i in range(n-1,0,-1) ]
