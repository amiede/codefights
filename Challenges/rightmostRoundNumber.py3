# https://codefights.com/challenge/npgAxzzMjLxhaXwSM/
#def rightmostRoundNumber(a):
a, = eval(dir()[0])
for i in range(len(a))[::-1]:
    if a[i] % 10 == 0:
        return i
return -1