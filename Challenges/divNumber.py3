# https://app.codesignal.com/challenge/hJWTa9EzRsQFKF5Ju
#def divNumber(k, l, r):
k, l, r = eval(dir()[0])
s = 0
for i in range(l, r+1):
    t = [i]
    for d in range(1, i):   
        if i % d == 0:
            t += [d]
    if len(t) == k:
        s += 1
return s


# Solution by duckalisk
#r = range
#divNumber = lambda k, a, b: sum(sum(n%~d == 0 for d in r(n)) == k for n in r(a, b+1))