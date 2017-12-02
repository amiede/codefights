# https://codefights.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def matrixElementsSum(matrix):
    shadowColumns = [False] * len(matrix[0])
    theSum = 0
    
    for row in matrix:
        for col, item in enumerate(row):
            if item == 0:
                shadowColumns[col] = True
            elif shadowColumns[col] == False:
                theSum += item 
    
    return theSum