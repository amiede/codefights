# https://app.codesignal.com/challenge/i7AAfRDur9TybJQ2P 
# https://en.wikipedia.org/wiki/Polynomial#Calculus
# f'(x) = b * x ^ n
# f(x) = b / (n + 1) * x ^ (n + 1) 
def computeDefiniteIntegral(l, r, P):
    s = 0 
    for i, v in enumerate(P): 
        s += ig(v,i,r) - ig(v,i,l)
    return s
    
def ig(b,n,x):
    return ( (b/(n+1)) * (x**(n+1)) )    