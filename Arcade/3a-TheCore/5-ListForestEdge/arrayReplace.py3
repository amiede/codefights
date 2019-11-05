# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/mCkmbxdMsMTjBc3Bm
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    
    # Short version: list comprehension
    return [ substitutionElem if e == elemToReplace else e for e in inputArray ]
    
    # Long version: Looping
    '''
    for i, e in enumerate(inputArray):
        if e == elemToReplace:
            inputArray[i] = substitutionElem
    
    return inputArray
    '''