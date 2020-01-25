# https://app.codesignal.com/arcade/code-arcade/well-of-integration/fzsCQGYbxaEcTr2bL
# https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
def allLongestStrings(inputArray):
    m = len(max(inputArray, key=len))
    return [ i for i in inputArray if len(i) == m ]