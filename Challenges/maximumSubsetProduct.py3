# https://app.codesignal.com/challenge/gnc8fMQSsxshLj9BY
#def maximumSubsetProduct(a):
a, = eval(dir()[0])

t = [ x for x in a if x < 0 ] 
l = len(t)

if len(a) == 1 or l == 0 or l % 2 == 0:
    return 1
else:
    return max(t)