# https://codefights.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE
def isBeautifulString(inputString):
    
    # Count each letter in inputString
    counter = dict.fromkeys(string.ascii_lowercase, 0)
    
    for char in sorted(inputString):
        counter[char] += 1

    # Check letter counts
    charList = sorted(counter.keys()) # sorted list of keys (a, b, c, ...)
    
    # Iterate over sorted key list (alphabet)
    for i in range(len(charList)-1):
        # And compare counted letters
        if counter[charList[i+1]] > counter[charList[i]]:
            return False
    
    return True