# https://app.codesignal.com/challenge/PG2nQ9fDwfhhyBEQn
#def arithmeticExpression(a, b, c):
# 89
a, b, c, *R = eval(dir()[0]) # *R --> R = []
for o in ["+", "-", "*", "/"]:
    R += [ eval("%s%s%s" % (a, o, b)) == c ]
return any(R)