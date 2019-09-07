# https://app.codesignal.com/challenge/nckaDwhQf2gb4HFhS
#def evenDigitsOnly(n):
n, = eval(dir()[0])
return len([d for d in str(n) if int(d) % 2 == 0]) == len(str(n))