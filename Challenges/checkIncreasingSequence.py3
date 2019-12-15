# https://app.codesignal.com/challenge/smCFaPQFYvQc2xuxk
#def checkIncreasingSequence(s):
s, = eval(dir()[0])
# The all() method returns True when all elements in 
# the given iterable are true. If not, it returns False. 
# zip for shorthand to access current and next element
return all( i < j for i, j in zip(s, s[1:]) )


# shorthand to access current and next element
#for i, j in zip(s, s[1:]):
#    if i >= j:
#        return False
#
#return True

#Solution by synth
#e, = eval(dir()[0])
#return sorted({*e}) == e