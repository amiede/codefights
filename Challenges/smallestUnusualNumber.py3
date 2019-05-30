# https://app.codesignal.com/challenge/x8ZtsmZicqwSa2FjZ
#def smallestUnusualNumber(a):

# convert a (string) to int list of digits 
n = list(map(int, *eval(dir()[0])))
s = sum(n) # cross sum
p = 1

# calculate product
for i in sorted(n): # sorted to speed things up
    if i == 0: # shortcut: 0 kills product
        break
    p *= i
    if p >= s: # stop if exceeded
        return 10 - n[-1]           

return 0