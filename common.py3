# Initialize 2D array
array2D = [ [0] * n for x in range(n) ]

# Convert integer to digits list
def numberToDigits(n):
    return [ int(i) for i in str(n) ]
	return list(map(int, str(num)))
# alternatively divide by 10, 100, ... ;-)
	
# Convert a list of int digits to an integer
def digitsToNumber(digitsList):
    return int(''.join((map(str, digitsList))))

# Access row and column in matrix (nested lists)
[ r[b] for r in matrix ] # column b
matrix[a] # row a

# Character-saving workaround (Challenges/Python)
# return sorted(*eval(dir()[0]), key=len)
# w,d = eval(dir()[0])
# (a, b, c), (d, e, f) = eval(dir()[0])
# vars() --> dict of input parameters
# swapCase = str.swapcase

# 
if b > a:
    a, b = b, a

# short function
# r = range

# n, *r = eval(dir()[0])
#same as? --> r = []
# return r

# Fastest way to copy
t = l[:]  

# Add to list shorthand
R.append(a) --> R += [a] # but beware

# shorthand to access current and next element
i < j for i, j in zip(s, s[1:])
for i, j in zip(s, s[1:]):


#********************************************
# Character-saving workaround (Challenges/Coffee)
# [x
# n] = args
#********************************************