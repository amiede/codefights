# https://app.codesignal.com/challenge/53DMcWRBbZMdsF6vm
#def quasifactorial(n):
    
r = 1

for i in range(2,eval(dir()[0])[0]+1):
    r *= i
    r -= 1

return r


# Solution by duckalisk
#f = quasifactorial = lambda n: 1//n or n*f(n-1) - 1