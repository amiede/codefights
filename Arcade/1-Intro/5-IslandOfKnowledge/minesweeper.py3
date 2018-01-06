# https://codefights.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
# Took my solution from this challenge
# https://codefights.com/challenge/48o3YSHdmHtWRTxNT
def minesweeper(m):
    n = [(-1, -1), (-1, 0), (-1, 1),
         ( 0, -1),          ( 0, 1),
         ( 1, -1), ( 1, 0), ( 1, 1)] 

    r = len(m)
    c = len(m[0])
    
    s = [[0 for i in range(c)] for j in range(r)]
    
    for i in range(r):
        for j in range(c):
            if m[i][j] == True:
                for f, g in n:
                    x = i + f
                    y = j + g
                    if x > -1 and x < r and y > -1 and y < c:
                        s[x][y] += 1                      
             
    return s
