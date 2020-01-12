# https://app.codesignal.com/challenge/j9JSTTntsnq8xRCgZ
#def extractEachKth(a, k):
a,k = eval(dir()[0])
return [ e for i, e in enumerate(a) if i not in range(k-1, len(a), k) ]


#a,k = eval(dir()[0])
#return [ a[i-1] for i in range(len(a)+1) if i % k != 0 ]


# Solution by duckalisk
#a, k = eval(dir()[0])
#del a[k-1::k]
#return a