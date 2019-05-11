# https://app.codesignal.com/challenge/s4AfxmEgtJdA9ANJr
#def isArithmeticProgression(s):
s, = eval(dir()[0])
d = 0

for i in range(len(s)-1):
    t = s[i] - s[i+1]

    if d != 0 and d != t:
        return 0

    d = t

return 1    