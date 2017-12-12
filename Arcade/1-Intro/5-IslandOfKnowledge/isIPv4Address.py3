# https://codefights.com/arcade/intro/level-5/veW5xJednTy4qcjso/
# Clumsy solution
def isIPv4Address(inputString):

    # Biggest mistakes sorted out first
    # Characters contained
    for c in inputString: 
        if c in string.ascii_lowercase: return False
        
    # Dots at beginning or end
    if inputString[0] == "." or inputString[-1] == ".": return False
    
    # Wrong number of dots
    if inputString.count(".") != 3: return False
    
    # Getting the blocks
    blocks = inputString.split(".")
    if "" in blocks: return False # Empty block
    
    # This works only if there are no empty blocks
    blocks = [int(x) for x in blocks]
    
    # Within range
    if max(blocks) > 255: return False
    
    return True