# https://app.codesignal.com/arcade/code-arcade/well-of-integration/QmK8kHTyKqh8xDoZk
def threeSplit(a):

    goal = sum(a)/3
    result = currentSum = temp = 0
    
    for i in range(len(a) - 1):
        currentSum += a[i]

        if currentSum == goal:
            temp += 1
        
        if currentSum == 2 * goal:
            result += temp
            if goal == 0:
                result -= 1
    
    return result

