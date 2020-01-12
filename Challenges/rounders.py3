# https://app.codesignal.com/challenge/Axe2EhL7bpvqDX9bF
#def rounders(n):
n, = eval(dir()[0])
t = 1
while n > 10:
    n = (n + 5) // 10
    t *= 10
return t * n


# Solution by synth
#rounders = r = lambda a: a>9 and 10*r((a+5)//10) or a