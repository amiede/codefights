# https://app.codesignal.com/challenge/Rrq7MRnYKFhCGooeg
#def makeArrayConsecutive(sequence):
# 61
A, = eval(dir()[0])
return [ i for i in range(min(A), max(A)) if i not in A ]

# 71
#A, *R = eval(dir()[0])
##R = [] # *R initilizes 
#for i in range(min(A), max(A)+1):
#    if i not in A:
#        R += [i]
#return R