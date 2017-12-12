# https://codefights.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
def arrayMaximalAdjacentDifference(inputArray):

    diffs = []
    
    for i in range(0,len(inputArray)-1):
        diffs.append(abs(inputArray[i]-inputArray[i+1]))
    
    return max(diffs)