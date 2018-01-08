# https://codefights.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ/
def circleOfNumbers(n, firstNumber):
    # Opposite is half the total away
    oppCandidate = firstNumber + (n/2)
    
    # Special case: over circle origin
    if oppCandidate >= n:
        oppCandidate -= n
    
    return oppCandidate