# https://app.codesignal.com/challenge/uFMZ9Wm3MK3f7j5uG
#def bishopAndPawn(bishop, pawn):
(a, c), (b, d) = eval(dir()[0])
# x-difference to the pawn must be same as the y-difference 
# (on diagonal with respect to bishop)
return abs(ord(a) - ord(b)) == abs(int(c) - int(d))

# Solutions by hamza_a16
#def bishopAndPawn(bishop, pawn):

# # 73
# b,p=eval(dir()[0])
# a,d=b
# c,e=p
# return (ord(a)-ord(c))/(int(e)-int(d)) in [1,-1]

# # 72
# b,p=eval(dir()[0])
# o=ord
# return (o(b[0])-o(p[0]))/(o(b[1])-o(p[1])) in [1,-1]

# # 58
# b,p=eval(dir()[0])
# a,c,d,e=map(ord,b+p)
# return a-d in (c-e, e-c)

# # 58
b,p=eval(dir()[0])
a,c,d,e=map(ord,b+p)
return a-d in (e-c, c-e)
