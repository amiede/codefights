# https://codefights.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
def arrayMaxConsecutiveSum(inputArray, k):
    
    firstSum = 0
    maxSum = 0
    
    # Sum the first k numbers
    # Short Python version: 
    #firstSum = sum(inputArray[:k])
    for i in range(k): 
        firstSum += inputArray[i]
    
    maxSum = firstSum

    # Iterate from k to the end of the input list
    for i in range(k, len(inputArray)):
        # Subtract (remove) first element and add current one
        firstSum = firstSum - inputArray[i-k] + inputArray[i]
        maxSum = max(maxSum, firstSum)
            
    return maxSum
    
    ''' Helpful comment by user "implication":
    Best way to approach this problem is through a Dynamic Programming Approach, only update the maximum sum as NECESSARY. Solution should be in O(n) time, to avoid the time limit error, not in O(n^2) by running an initial loop to get the first sum of k values then updating the value to keep the total number of added numbers to be k.
    '''            