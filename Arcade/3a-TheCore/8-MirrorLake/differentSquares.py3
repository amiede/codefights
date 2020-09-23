# https://app.codesignal.com/arcade/code-arcade/mirror-lake/fQpfgxiY6aGiGHLtv
# https://codefights.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv
def differentSquares(matrix):

    diffSquares = []
    
    # Check all squares
    for i in range(len(matrix) - 1): # rows
        for j in range(len(matrix[0]) - 1): # columns
            currSquare = [ matrix[i][j], [matrix[i+1][j], matrix[i][j+1]], matrix[i+1][j+1] ]
            if currSquare not in diffSquares: # <3 Python
                diffSquares.append(currSquare)
    
    return len(diffSquares)