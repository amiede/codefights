# https://codefights.com/arcade/intro/level-12/tQgasP8b62JBeirMS
# Rather clumsy solution 
def sudoku(grid):
    
    # What we check against
    correctSet = {1,2,3,4,5,6,7,8,9}
    
    # Index offset to access all sub-grids
    subOffset = [  (0,0), (0,3), (0,6),
                   (3,0), (3,3), (3,6),
                   (6,0), (6,3), (6,6) ]
    
    # Check the sub-grids
    for o in subOffset:
        temp = []
        for i in range(3):
            for j in range(3):
                # Collect all the numbers
                temp.append(grid[i + o[0]][j + o[1]])
        # Collected numbers do not match the correct set
        if len(correctSet - set(temp)) != 0:
            return False

    # Check the rows
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(grid[i][j])
        if len(correctSet - set(temp)) != 0:
            return False 

    # Check the columns
    for j in range(9):
        temp = []
        for i in range(9):
            temp.append(grid[i][j])
        if len(correctSet - set(temp)) != 0:
            return False 
           
    return True