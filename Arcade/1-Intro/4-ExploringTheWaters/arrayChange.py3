# https://codefights.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example
For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''
def arrayChange(inputArray):

    counter = 0
    
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            diff = abs(inputArray[i+1]-inputArray[i]) + 1
            inputArray[i+1] += diff
            counter += diff
        
    return counter