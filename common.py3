# Initialize 2D array
array2D = [ [0] * n for x in range(n) ]

# Convert integer to digits list
def numberToDigits(n):
    return [ int(i) for i in str(n) ]
	return list(map(int, str(num)))
# alternatively divide by 10, 100, ... ;-)

# Digit sum
sum(map(int, str(number)))
sum(int(digit) for digit in str(number))

	
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
# return f"Hello, {eval(dir()[0])[0]}"


#Ternary return
# return n if n<m else m
# Ternary if elif else
# expr1 if condition1 else expr2 if condition2 else expr
# ternary shortcut
# a = true  && 5 || 10

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
# return args[0].replace /\B/g, "-"
#********************************************