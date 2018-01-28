# https://codefights.com/arcade/intro/level-11/o2uq6eTuvk7atGadR
def lineEncoding(s):
    
    newString = ""
    charCounter = 1
    
    # This always misses the last char, so let's add one
    s += "$"
    for i in range(1,len(s)):
        # Consecutive characters
        if s[i] == s[i-1]:
            charCounter += 1
        else: # Done, make prefix
            if charCounter > 1:
                newString += str(charCounter) 
            
            newString += s[i-1]
            charCounter = 1
    
    return newString