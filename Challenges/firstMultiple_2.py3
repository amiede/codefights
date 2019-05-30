# https://app.codesignal.com/challenge/JFQCeSKZpP8pAeHSB
# Solution by dung_l2
#def firstMultiple(D, s):
d, s = eval(dir()[0])
while any(s % x for x in d): 
    # if all(s % x < 1 for x in d):
    # if not sum(s % i for i in d):
    # if not sum(map(lambda x: s % x, d)):
        # return s
    s += 1    
return s