# https://app.codesignal.com/challenge/cCp2KatYhxeXPtG7a
# Solution by dung_l2
#def neighboringCells(matrix):
m, = eval(dir()[0])
x = len(m)
for i in range(x):
  y = len(m[i])
  for j in range(y):
    if i != x - 1:
      m[i][j] += 1
    if i:
      m[i][j] += 1
    if j != y - 1:
      m[i][j] += 1
    if j:
      m[i][j] += 1

return m