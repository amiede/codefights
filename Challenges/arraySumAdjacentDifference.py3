# https://app.codesignal.com/challenge/h7i7qTRoon4KSekYk
#def arraySumAdjacentDifference(A):
A, = eval(dir()[0])

S = []

for i in range(len(A)-1):
    S.append(abs(A[i]-A[i+1]))

return sum(S)