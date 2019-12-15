# https://app.codesignal.com/challenge/hJWTa9EzRsQFKF5Ju
# Solution by duckalisk
#def divNumber(k, l, r):
r = range
divNumber = lambda k, a, b: sum(sum(n%~d == 0 for d in r(n)) == k for n in r(a, b+1))