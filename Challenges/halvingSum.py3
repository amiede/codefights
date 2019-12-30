# https://app.codesignal.com/challenge/mJPidEuuPJ8vCh6sh
#def halvingSum(n):
# 42     
n, = eval(dir()[0])    
h = n
while n:
    n /= 2 # better/safer //=
    h += n
return h

# 60
#n, = eval(dir()[0])
#return sum([ n/2**i for i in range(int(n**0.5)) ]) # better/safer //

# Solution by synth
# 34
# h = halvingSum = lambda a: a and a+h(a//2)