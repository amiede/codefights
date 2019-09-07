# https://app.codesignal.com/challenge/hTvQiQuJTk9bSvY6n
# Classic variant
def fibonacciNumber(n):        
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciNumber(n-2) + fibonacciNumber(n-1)