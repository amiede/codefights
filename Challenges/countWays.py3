# https://app.codesignal.com/challenge/a8GNsYr8FQxZmMhJj
#def countWays(n, k):
# 74
f = math.factorial
countWays = lambda n, k: 0 if k > n else f(n) // f(k) // f(n-k) % (10**9 + 7) #1000000007


# Solution by synth
# 63
#import scipy.special as s
#return  s.comb(*eval(dir()[0]), 1) % (10**9 + 7) # 1 --> exact=True