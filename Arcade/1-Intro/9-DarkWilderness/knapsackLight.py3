# https://codefights.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2
def knapsackLight(value1, weight1, value2, weight2, maxW):
    # What a mess!
    if (weight1 + weight2) <= maxW:
        return (value1 + value2)  
    if weight1 <= maxW:
        if value1 > value2: 
            return value1
        elif weight2 > maxW:
            return value1
    if weight2 <= maxW:
        return value2
    else:
        return 0
