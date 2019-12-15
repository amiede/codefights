# https://app.codesignal.com/challenge/Axe2EhL7bpvqDX9bF
# Solution by synth
#def rounders(n):
rounders = r = lambda a: a>9 and 10*r((a+5)//10) or a