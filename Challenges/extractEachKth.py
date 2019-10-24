# https://app.codesignal.com/challenge/j9JSTTntsnq8xRCgZ
#def extractEachKth(inputArray, k):
a,k = eval(dir()[0])
return [ a[i-1] for i in range(len(a)+1) if i % k != 0 ]