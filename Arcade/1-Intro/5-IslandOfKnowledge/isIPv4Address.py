# https://codefights.com/arcade/intro/level-5/veW5xJednTy4qcjso/
def isIPv4Address(inputString):
    # Wrong number of dots
    if inputString.count(".") != 3: return False
    
    # Getting the blocks
    # This works only if the blocks are integers
    try:
        blocks = [int(x) for x in inputString.split(".")]
    except ValueError: 
        return False
    
    # Within range
    if max(blocks) > 255: return False
    
    return True