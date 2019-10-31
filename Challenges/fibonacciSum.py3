# https://app.codesignal.com/challenge/F54etL8JkcJtQpKAZ
#def fibonacciSum(n):
# Generate n Fibonacci numbers
def f(n):
    x, y = 1, 1 
    r = []
    
    for _ in range(n-1):
        x, y = y, x + y
        r += [ x ] # beware
        #r.append(x)
        
    return r

n, = eval(dir()[0])
    
# should be enough for guaranteed constraints
t = [ i for i in f(19) if i <= n ][::-1]
r = []

# one trick is to go from largest Fibonaccis to smallest
# skipping the ones to large for the sum
for i in range(len(t)):
    if sum(r) + t[i] <= n:
        r += [ t[i] ] # beware
        #r.append(t[i])

return r[::-1]
