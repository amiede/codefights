# https://app.codesignal.com/challenge/9EYdtrq7ZytJy6Fy4
def specialPolynomial(x, n):
    
    s = 0
    
    for k in range(999): # sys.maxsize
        s += x**k
    
        if s > n: # one step too far
            return k-1