# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/aFF9HDm2Rsti9j5kc
def isInfiniteProcess(a, b):
    
    # b is greater or difference not divisible by 2
    if (a > b) or (b-a)%2 != 0: 
        return True
    
    return False