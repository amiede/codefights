# https://app.codesignal.com/challenge/pvndueQwncJoTmDxK
#def crossingSum(m, a, b):
m, a, b = eval(dir()[0])    
# column b + row a - duplicate entry
return sum([ r[b] for r in m ] + m[a]) - m[a][b]

# crossingSum = lambda m,a,b: sum([ r[b] for r in m ] + m[a]) - m[a][b]