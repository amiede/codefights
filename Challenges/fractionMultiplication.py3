# https://app.codesignal.com/challenge/ptQ8nzNPHqbwbMoqn
#def fractionMultiplication(a, b):
(a, b), (c, d) = eval(dir()[0])
e = a * c
f = b * d
g = math.gcd(e, f)
return (e // g, f // g)

# Solution by synth
# 62
# [a,b], [c,d] = eval(dir()[0])
# a *= c
# b *= d
# c = math.gcd(a,b)
# return a/c, b/c