# https://codefights.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb
# Very similar to the minesweeper task or challenge
# https://codefights.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
# https://codefights.com/challenge/48o3YSHdmHtWRTxNT
# https://app.codesignal.com/challenge/b4eAriXPbJypzfeXL
#def chessKnightMoves(c):
c, = eval(dir()[0])
# Chess coordinates to array indices
pX, pY = int(c[1])-1, ord(c[0])-97

# Size of chess board
b = 8

# Possible moves
n = [(-2, 1), (-1,  2), 
     ( 1, 2), ( 2,  1), 
     (-2,-1), (-1, -2), 
     ( 1,-2), ( 2, -1)] 

m = 0

# Generate all moves for input
for x, y in n:
    mX = pX + x
    mY = pY + y
    # Count only the ones on the board
    if mX > -1 and mX < b and mY > -1 and mY < b:
        m += 1                      

return m
