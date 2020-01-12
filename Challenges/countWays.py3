# https://app.codesignal.com/challenge/a8GNsYr8FQxZmMhJj
#def countWays(n, k):
# 74
f = math.factorial
countWays = lambda n, k: 0 if k > n else f(n) // f(k) // f(n-k) % (10**9 + 7) #1000000007