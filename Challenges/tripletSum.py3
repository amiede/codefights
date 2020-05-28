# https://app.codesignal.com/challenge/vmftDFrAxwX7bGSzL
# With help from https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
#def tripletSum(x, a):
# 139
x, a = eval(dir()[0])
a.sort()
k = len(a)
for i in range(k):
    l = i + 1 # start left (right of i)
    r = k - 1 # start right

    # move together
    while (l < r): 
        s = a[i] + a[l] + a[r]
        if(s == x): 
            return True            
        elif (s < x): 
            l += 1
        else: # s > x 
            r -= 1

return False


# Time complexity too high
#import itertools as i
#x, a = eval(dir()[0])
##if a[0] > x:
##    return False
#for l in i.combinations(a, 3):
#    if sum(l) == x:
#        return True        
#return False