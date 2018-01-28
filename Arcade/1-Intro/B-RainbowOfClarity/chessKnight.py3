# https://codefights.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb
# Very similar to the minesweeper task or challenge
# https://codefights.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
# https://codefights.com/challenge/48o3YSHdmHtWRTxNT
def chessKnight(cell):
    # Chess coordinates to array indices
    posX, posY = int(cell[1])-1, ord(cell[0])-97
    
    # Size of chess board
    sizeBoard = 8
    
    # Possible moves
    n = [(-2, 1), (-1,  2), 
         ( 1, 2), ( 2,  1), 
         (-2,-1), (-1, -2), 
         ( 1,-2), ( 2, -1)] 
   
    numValidMoves = 0
    
    # Generate all moves for input
    for x, y in n:
        mX = posX + x
        mY = posY + y
        # Count only the ones on the board
        if mX > -1 and mX < sizeBoard and mY > -1 and mY < sizeBoard:
            numValidMoves += 1                      
             
    return numValidMoves