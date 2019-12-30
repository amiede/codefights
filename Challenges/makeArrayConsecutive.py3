# https://app.codesignal.com/challenge/Rrq7MRnYKFhCGooeg
#def makeArrayConsecutive(sequence):
A, *R = eval(dir()[0])
#R = [] # *R initilizes 
for i in range(min(A), max(A)+1):
    if i not in A:
        R += [i]
return R