# https://app.codesignal.com/challenge/YZkenvHqAjS9fh7HM
# Solution by miguel_r58
#def oddNumbersBeforeZero(S):
m = 0
for e in eval(dir()[0])[0]:
    m += e&1
    if e < 1:
        return m