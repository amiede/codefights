# https://app.codesignal.com/challenge/i7AAfRDur9TybJQ2P 
# https://en.wikipedia.org/wiki/Polynomial#Calculus
# f'(x) = b * x ^ n
# f(x) = b / (n + 1) * x ^ (n + 1) 
def computeDefiniteIntegral(l, r, P):
    s = 0 
    for i, v in enumerate(P): 
        s += (v/(i+1)) * ((r)**(i+1) - (l)**(i+1))
    return s 