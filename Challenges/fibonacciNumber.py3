# https://app.codesignal.com/challenge/hTvQiQuJTk9bSvY6n
# https://de.wikipedia.org/wiki/Fibonacci-Folge#Formel_von_Moivre-Binet
def fibonacciNumber(n):        
    x = (1/math.sqrt(5)) * (((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)
    return int(abs(x))


# Classic variant
#def fibonacciNumber(n):        
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fibonacciNumber(n-2) + fibonacciNumber(n-1)	


# Solution by duckalisk
#return round(.447/.618**eval(dir()[0])[0])