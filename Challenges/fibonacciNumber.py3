# https://app.codesignal.com/challenge/hTvQiQuJTk9bSvY6n
# https://de.wikipedia.org/wiki/Fibonacci-Folge#Formel_von_Moivre-Binet
def fibonacciNumber(n):        
    x = (1/math.sqrt(5)) * (((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)
    return int(abs(x))