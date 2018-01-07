# https://codefights.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
# Does not fit the time limit
def arrayMaxConsecutiveSum(inputArray, k):

    maxSum = 0
    
    for i in range(0,len(inputArray)-k+1):
        sum = 0
        for j in range(0,k):
            sum += inputArray[i+j]
            #print(sum)
        
        if sum > maxSum: maxSum = sum
        #print(maxSum)
        
    return maxSum