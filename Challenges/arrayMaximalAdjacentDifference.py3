# https://app.codesignal.com/challenge/8cWAm3sYiBSNXwMZ7
# https://codefights.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
#def arrayMaximalAdjacentDifference(inputArray):
A, = eval(dir()[0])

D = []

for i in range(len(A)-1):
    D.append(abs(A[i]-A[i+1]))

return max(D)