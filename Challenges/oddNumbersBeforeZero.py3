# https://app.codesignal.com/challenge/YZkenvHqAjS9fh7HM
#def oddNumbersBeforeZero(S):
S, = eval(dir()[0])
return len([ i for i in S[:S.index(0)] if i % 2 ])