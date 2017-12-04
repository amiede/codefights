# https://codefights.com/challenge/GrnTbWrj62B6AJXag
def findNthSmallestMultipleInArray(a,n):   
    return min(a)*n
    # Clumsy solution ;-)
    #sM = [x*n for x in a]
    #return min(sM)  