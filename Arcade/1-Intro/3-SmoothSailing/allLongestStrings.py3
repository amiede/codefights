# https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
def allLongestStrings(inputArray):

    longest = max(len(s) for s in inputArray)
    newList = []
    
    for string in inputArray:
        if len(string) == longest:
            print(string)
            newList.append(string)
            
    return newList