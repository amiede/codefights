# https://app.codesignal.com/challenge/YZkenvHqAjS9fh7HM
#def oddNumbersBeforeZero(S):
S, = eval(dir()[0])
return len([ i for i in S[:S.index(0)] if i % 2 ])


# Solution by miguel_r58
#m = 0
#for e in eval(dir()[0])[0]:
#    m += e&1
#    if e < 1:
#        return m