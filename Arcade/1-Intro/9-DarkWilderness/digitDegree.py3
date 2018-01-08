# https://codefights.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo
def digitDegree(n):
    digitSum = n # German: Quersumme
    iterations = 0
    
    while digitSum > 9:
        digits = numberToDigits(digitSum)
        digitSum = sum(digits) # German: Quersumme
        iterations += 1
    
    return iterations
        
def numberToDigits(n):
    return [ int(i) for i in str(n) ]