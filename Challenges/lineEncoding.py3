# https://app.codesignal.com/challenge/wBBHdf8aSNd4q9ECZ
# https://codefights.com/arcade/intro/level-11/o2uq6eTuvk7atGadR 
def lineEncoding(s):
 
    n = ""
    c = 1
    
    # This always misses the last char, so let's add one
    s += "$"
    for i in range(1,len(s)):
        # Consecutive characters
        if s[i] == s[i-1]:
            c += 1
        else: # Done, make prefix
            if c > 1:
                n += str(c) 
            
            n += s[i-1]
            c = 1
    
    return n
    
    
    
    
    #m = re.compile(r'(\w)\1*')
    #print([match.group() for match in m.finditer(s)])