# https://app.codesignal.com/challenge/JFQCeSKZpP8pAeHSB
#def firstMultiple(D, s):
D,s = eval(dir()[0])
for i in range(s,999): # 10**6
    t = 1 # True

    for d in D:
        if i % d != 0:
            t = 0 # False

    if t: 
        return i