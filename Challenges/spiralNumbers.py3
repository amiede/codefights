# https://codefights.com/arcade/intro/level-12/uRWu6K8E7uLi3Qtvx
# https://app.codesignal.com/challenge/JiFpoZHM4ogdn5xQc
#def spiralNumbers(n):
n, = eval(dir()[0])
D = [ (0,1), (1,0), (0,-1), (-1,0) ]
cD = 0
cP = (0, 0)
r = [ [0] * n for x in range(n) ]

for i in range(1, n * n + 1):
    r[cP[0]][cP[1]] = i
    nP = cP[0] + D[cD][0], cP[1] + D[cD][1]
    if not (0 <= nP[0] < n and
            0 <= nP[1] < n and
            r[nP[0]][nP[1]] == 0):
        cD = (cD + 1) % 4
        nP = cP[0] + D[cD][0], cP[1] + D[cD][1]
    cP = nP

return r
