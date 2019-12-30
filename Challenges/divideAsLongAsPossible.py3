# https://app.codesignal.com/challenge/WCisYsTSeF4Kqwzs7
#def divideAsLongAsPossible(n, d):
# 41
n, d = eval(dir()[0])
while n % d == 0:
    n /= d

return n