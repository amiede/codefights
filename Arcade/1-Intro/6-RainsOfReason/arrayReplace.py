# https://codefights.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm/
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if elem == elemToReplace else elem for elem in inputArray]