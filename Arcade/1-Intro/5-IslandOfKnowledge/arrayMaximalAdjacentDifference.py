# https://codefights.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
def arrayMaximalAdjacentDifference(inputArray):

    maxDiff = 0
    currDiff = 0
    
    for i in range(0,len(inputArray)-1):
        currDiff = abs(inputArray[i]-inputArray[i+1])
        if currDiff > maxDiff:
            maxDiff = currDiff
    
    return maxDiff