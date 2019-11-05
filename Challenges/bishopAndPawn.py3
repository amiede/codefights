# https://app.codesignal.com/challenge/uFMZ9Wm3MK3f7j5uG
#def bishopAndPawn(bishop, pawn):
(a, c), (b, d) = eval(dir()[0])
# x-difference to the pawn must be same as the y-difference 
# (on diagonal with respect to bishop)
return abs(ord(a) - ord(b)) == abs(int(c) - int(d))