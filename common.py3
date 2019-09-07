# Initialize 2D array
array2D = [ [0] * n for x in range(n) ]

# Convert integer to digits list
def numberToDigits(n):
    return [ int(i) for i in str(n) ]
# alternatively divide by 10, 100, ... ;-)
	
# Convert a list of int digits to an integer
def digitsToNumber(digitsList):
    return int(''.join((map(str, digitsList))))

# Character-saving workaround (Challenges/Python)
# return sorted(*eval(dir()[0]), key=len)
# w,d = eval(dir()[0])
# (a, b, c), (d, e, f) = eval(dir()[0])
# vars() --> dict of input parameters
# swapCase = str.swapcase

#********************************************
# Character-saving workaround (Challenges/Coffee)
# [x
# n] = args
#********************************************