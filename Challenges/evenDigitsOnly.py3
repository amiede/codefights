# https://app.codesignal.com/challenge/nckaDwhQf2gb4HFhS
#def evenDigitsOnly(n):
n, = eval(dir()[0])
return len([d for d in str(n) if int(d) % 2 == 0]) == len(str(n))


# Solution by sil1
#return sum(x in '13579' for x in str(vars()))<1