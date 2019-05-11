#def VedicTwoDigitMultiplication(a, b):
# Solution by gabor_p
a,c = eval(dir()[0])
b = a%10
a /= 10
d = c%10
c /= 10
return a*c, a*d+b*c, b*d