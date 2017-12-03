# https://codefights.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
def isLucky(n):
    # Convert int to string, make list of digits
    intList = [int(i) for i in str(n)]
    
    # Find the middle
    middle = len(intList)//2
    
    return True if (sum(intList[:middle]) == sum(intList[middle:])) else False