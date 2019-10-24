# https://app.codesignal.com/challenge/j9JSTTntsnq8xRCgZ
#def extractEachKth(a, k):
a,k = eval(dir()[0])
return [ e for i, e in enumerate(a) if i not in range(k-1, len(a), k) ]