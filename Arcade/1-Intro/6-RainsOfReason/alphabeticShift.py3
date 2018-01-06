# https://codefights.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui
def alphabeticShift(inputString):
   
    outputString = ""
    
    for c in inputString:
        outputString += chr(ord(c)+1)
        
    return outputString.replace("{", "a")