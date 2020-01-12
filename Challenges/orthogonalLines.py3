# https://app.codesignal.com/challenge/7CAwSYffiBwCP5on7
#def orthogonalLines(l, m):
l,m = eval(dir()[0])    
#return (l[0]*m[0] + l[1]*m[1]) == 0
return l[0]*m[0] == -l[1]*m[1] 


# Solution by adavis
#(a, b, c), (d, e, f) = eval(dir()[0])
#return a*d == -b*e