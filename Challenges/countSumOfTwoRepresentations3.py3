# https://app.codesignal.com/challenge/mXCWzh37ibxEY822h
# 0 + n, 1 + n-1, 2 + n-2...
# --> n//2 + 1 ways to represent n
#def countSumOfTwoRepresentations3(n, l, r):
# 68
n, l, r = eval(dir()[0])
return sum([ 1 for i in range(n//2+1) if i >= l and n-i <= r ])

# 77
#n, l, r, *T = eval(dir()[0])
#for i in range(n//2+1):
#    if i >= l and n-i <= r:
#        T += [1]
#return sum(T)


# Solution by synth 
# 50
#n, l, r = eval(dir()[0])
#return max(0, 1 + n//2 - max(l, n-r))