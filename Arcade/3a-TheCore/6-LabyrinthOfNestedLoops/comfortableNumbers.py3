# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pNfGgNk46YZ4c4RW5
# Thanks to the_mole ;-)
def sumOfDigits(number):
    return sum(int(digit) for digit in str(number))

# Comfortable means that A is not the same as B, 
# and A lies between [B - sumOfDigits(B), B + sumOfDigits(B)].
def isComfortable(a, b):
    if a == b:
        return False
    else:
        return (a >= b - sumOfDigits(b)) and (a <= b + sumOfDigits(b))
    
# Mutually comfortable means that A is comfortable with B 
# and B is comfortable with A
def areMutuallyComfortable(a, b):
    return isComfortable(a, b) and isComfortable(b, a)    

# Find pairs of numbers, contained between L and R, 
# such that numbers in those pairs are mutually comfortable
def comfortableNumbers(l, r):
    
    count = 0
    
    for a in range(l, r + 1):
        for b in range (a + 1, r + 1):
            if areMutuallyComfortable(a, b):
                count += 1
    
    return count
