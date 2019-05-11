# https://app.codesignal.com/challenge/E9FdTL6H2qa2bBjJp
#def maxSubmatrixSum(M, n, m):
M, n, m = eval(dir()[0])

s = -99 # endsumme -sys.maxsize
r = len(M) # rows
c = len(M[0]) # columns

for i in range(r):
    if i + n > r: break # ich steh' hier gerade auf dem Schlauch
    for j in range(c):
        if j + m > c: break
        t = 0
        for h in range(n):
            for w in range(m):  
                t += M[i+h][j+w]    
        if t > s:
            s = t

return s