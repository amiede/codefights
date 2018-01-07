# https://codefights.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
def extractEachKth(inputArray, k):
    outputArray = []
    
    # Take only indices that cannot be divided by k
    for i in range(len(inputArray)):
        if (i+1) % k != 0:
            outputArray.append(inputArray[i])
        
    return outputArray