# https://app.codesignal.com/challenge/4Q84t9DNbTKYfThxm
#def magicalWell(a, b, n):
a, b, n = eval(dir()[0])    
return sum( (a + i) * (b + i) for i in range(n) )