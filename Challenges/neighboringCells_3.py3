# https://app.codesignal.com/challenge/cCp2KatYhxeXPtG7a
# Solution by duckalisk
#def neighboringCells(matrix):
m, = eval(dir()[0])

for _ in ' '*4:
    m = numpy.rot90(m)
    m[1:] += 1

return m

# Add 1 to all rows except first to count
# neighbors directly above. Rotate matrix
# 4 times to count in each direction.