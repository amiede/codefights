# https://app.codesignal.com/challenge/hDqJT8AqKJAQS4vEw
#def maxDivisor(l, r, d):
l,r,d = eval(dir()[0])
for i in range(r,l-1,-1):
    if i % d == 0:
        return i

return -1