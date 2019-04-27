# https://app.codesignal.com/challenge/i7AAfRDur9TybJQ2P 
# https://en.wikipedia.org/wiki/Polynomial#Calculus
# f'(x) = b * x ^ n
# f(x) = b / (n + 1) * x ^ (n + 1) 
#def computeDefiniteIntegral(l, r, P):
l, r, P = eval(dir()[0])    
s = i = 0 
for v in P: 
    i += 1
    s += v/i * (r**i - l**i)
return s 