# https://codefights.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
def avoidObstacles(inputArray):
    # List for counting the non-divisors per obstacle
    potentialJumperList = [ 0 ] * max(inputArray) 
    
    # Count how often the members of the inputArray cannot
    #  be divided by each potential jumper
    for n in inputArray:
        for i in range(0, max(inputArray)):
            if n % (i+1) != 0: 
                potentialJumperList[i] += 1    
    
    # Collect those jumpers that cannot be divided by ALL 
    # members of the inputArray => count == len(inputArray)
    jumperList = []
    for i,n in enumerate(potentialJumperList):
        if n == len(inputArray):
            jumperList.append(i+1)
    
    # Smallest member is our goal, if there is no jumper (empty list)
    # we have to go above the largest member of the inputArray
    if jumperList: return min(jumperList) 
    else: return max(inputArray)+1