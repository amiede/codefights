# https://codefights.com/arcade/intro/level-11/Zr2XXEpkBPtYWqPJu
def isDigit(symbol):
    digits = "0123456789" # shorter: string.digits
    return symbol in digits
    
    # built-in solution:
    # return symbol.isdigit()