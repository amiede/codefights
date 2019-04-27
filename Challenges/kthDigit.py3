# https://app.codesignal.com/challenge/ikrZ4ujnBmJoH5yG3
def kthDigit(n, k):
    l = [ int(i) for i in str(n) ]
    
    if len(l) < k:
        return -1
    else:
        return l[k-1]