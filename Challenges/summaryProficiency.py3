# https://app.codesignal.com/challenge/TerQ5PCqqCRaDYEiM
#def summaryProficiency(a, n, m):
A,n,m = eval(dir()[0])
s = 0

for i in range(len(A)):
    if A[i] >= m and n > 0:
        s += A[i]
        n -= 1
return s