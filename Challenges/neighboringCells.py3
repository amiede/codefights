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


# Solution by dung_l2
#def neighboringCells(matrix):
#m, = eval(dir()[0])
#x = len(m)
#for i in range(x):
#  y = len(m[i])
#  for j in range(y):
#    if i != x - 1:
#      m[i][j] += 1
#    if i:
#      m[i][j] += 1
#    if j != y - 1:
#      m[i][j] += 1
#    if j:
#      m[i][j] += 1
#
#return m


# Solution by duckalisk
#m, = eval(dir()[0])
#
#for _ in ' '*4:
#    m = numpy.rot90(m)
#    m[1:] += 1
#
#return m
# Add 1 to all rows except first to count
# neighbors directly above. Rotate matrix
# 4 times to count in each direction.