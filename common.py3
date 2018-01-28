# Convert integer to digits list
def numberToDigits(n):
    return [ int(i) for i in str(n) ]

# Convert a list of int digits to an integer
def digitsToNumber(digitsList):
    return int(''.join((map(str,digitsList))))