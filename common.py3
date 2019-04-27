# Initialize 2D array
array2D = [ [0] * n for x in range(n) ]

# Convert integer to digits list
def numberToDigits(n):
    return [ int(i) for i in str(n) ]

# Convert a list of int digits to an integer
def digitsToNumber(digitsList):
    return int(''.join((map(str, digitsList))))

# Character-saving workaround (Challenges/Python)
# return sorted(*eval(dir()[0]), key=len)
# w,d = eval(dir()[0])

#********************************************
# Character-saving workaround (Challenges/Coffee)
# [x
# n] = args
#********************************************