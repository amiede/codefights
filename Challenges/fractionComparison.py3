# https://app.codesignal.com/challenge/5vmC2veLB5rsTPeZC
#def fractionComparison(a, b):
# 73
(a, b), (c, d) = eval(dir()[0])
t = (a * d) / (b * c)
return "=" if  t == 1 else "<" if t < 1 else ">"


# 58 
# Solution by synth
#[a,b], [c,d] = eval(dir()[0])
#a /= c
#b /= d
#return '=><'[(a>b)-(a<b)]