# https://app.codesignal.com/arcade/code-arcade/mirror-lake/BLbGNY3kEcvKjBCFC
def numberOfClans(divisors, k):

    s = set()
    
    for i in range(1, k+1):
            temp = ""
            for d in divisors:
                
                if i % d == 0:
                    temp += "1"
                else:
                    temp += "0"

            s.add(temp)
                    
    return len(s)