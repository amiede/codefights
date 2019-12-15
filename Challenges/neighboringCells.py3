# https://app.codesignal.com/challenge/cCp2KatYhxeXPtG7a
#def neighboringCells(matrix):
m, = eval(dir()[0])
n = [          (-1, 0),  
     ( 0, -1),          ( 0, 1),
               ( 1, 0)] 

r = len(m)
c = len(m[0])

for i in range(r):
    for j in range(c):
        for f, g in n:
            x = i + f
            y = j + g
            if x > -1 and x < r and y > -1 and y < c:
                m[x][y] += 1 

return m