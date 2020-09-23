# https://app.codesignal.com/arcade/code-arcade/mirror-lake/EeKpdMQXpBkgWjcvt
def constructSquare(s):

    # count how often each character occures
    c = sorted([s.count(x) for x in set(s)])
    
    # generator largest possible number based on string length
    mx = 0
    for i in range(len(s)):
        mx += 9*10**i
        
    # decrement from largest possible number and check squares
    while mx > 0:
        # is square
        if mx == math.isqrt(mx) ** 2:
            # count how often each digit occurs
            print(mx)
            cc = [str(mx).count(x) for x in set(str(mx))]
            # if the number of digits and number of character occurrences matches
            if sorted(cc) == c:
               return mx
        # at the end to catch the i-digits strings ;-)
        mx -= 1
                       
    return -1