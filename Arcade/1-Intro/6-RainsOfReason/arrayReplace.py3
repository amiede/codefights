# https://codefights.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm
def arrayReplace(inputArray, elemToReplace, substitutionElem):

    for i, elem in enumerate(inputArray):
        if elem == elemToReplace:
            inputArray[i] = substitutionElem
        
    return inputArray