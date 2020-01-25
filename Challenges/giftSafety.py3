# https://app.codesignal.com/challenge/ueMWmccxYbti63LXA
#def giftSafety(gift):
# 105
import itertools as i
giftSafety = lambda g: len([ 1 for t in zip(g, g[1:], g[2:]) if list(i.permutations(t)).count(t) > 1 ])


# 109
#import itertools as i
#g, = eval(dir()[0])
#return len([ 1 for t in zip(g, g[1:], g[2:]) if list(i.permutations(t)).count(t) > 1 ])


# 111
#import itertools as i
#g, = eval(dir()[0])
#c = 0
#for t in zip(g, g[1:], g[2:]):
#    if list(i.permutations(t)).count(t) > 1:
#        c += 1
#return c


# Solution by notch
# 59
giftSafety = lambda g: sum(len({*s}) < 3 for s in zip(g, g[1:], g[2:]))