# https://codefights.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
def checkPalindrome(inputString):
    
	strLength = len(inputString)
    
    for char in inputString[:int(strLength/2)]:
        strLength -= 1
        if char != inputString[strLength]:
            return False
    
    return True