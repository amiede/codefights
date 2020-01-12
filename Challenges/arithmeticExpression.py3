# https://app.codesignal.com/challenge/PG2nQ9fDwfhhyBEQn
#def arithmeticExpression(a, b, c):
# 56
a,b,c = eval(dir()[0])
return a + b == c or a - b == c or a * b == c or a / b == c

# 89
#a, b, c, *R = eval(dir()[0]) # *R --> R = []
#for o in ["+", "-", "*", "/"]:
#    R += [ eval("%s%s%s" % (a, o, b)) == c ]
#return any(R)


# Solution by synth
# 46
#a,b,c = eval(dir()[0])
#return c in (a*b, a/b, a+b, a-b)