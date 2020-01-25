# https://app.codesignal.com/challenge/o4P4CzeyHATP9xfm3
#def isPowerOfTwo2(n):

# http://graphics.stanford.edu/~seander/bithacks.html#DetermineIfPowerOf2
# 33
#n, = eval(dir()[0])
#return n & (n - 1) == 0

# 40
return bin(*eval(dir()[0])).count("1") == 1


# Solution by notch
# 29
# isPowerOfTwo2 = lambda n: n == n & -n 