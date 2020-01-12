# https://app.codesignal.com/challenge/r3f8PoCN4YCn634an
#def isPermutation(n, a):
n,a, = eval(dir()[0])
    
l = []

a.sort()

for i in range(n):
    l += [i+1]
    #l.append(i)

return l == a


#n,a, = eval(dir()[0])
#    
#l = list(range(1,n+1))
#
#a.sort()
#
#return l == a