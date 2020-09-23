# https://app.codesignal.com/arcade/code-arcade/mirror-lake/chW9F8bCgxYJBcgj3
def stringsConstruction(a, b):
    
    bLetters = dict()
    numberOfStrings = 0
    
    for l in b:
        bLetters[l] = bLetters.get(l, 0) + 1
    
    while sum(bLetters.values()) > 0:
        for l in a:
            if l in bLetters and bLetters[l] > 0:
                    bLetters[l] -= 1
            else:
                return numberOfStrings    
        numberOfStrings += 1
    
    return numberOfStrings 
    
    #return min(b.count(c)//a.count(c) for c in a)