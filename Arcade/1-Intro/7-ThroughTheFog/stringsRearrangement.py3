# https://codefights.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
import itertools # Thanks for learning about this
def stringsRearrangement(inputArray):
    # Make a list, as iterable can only be used once
    allPermutations = list(itertools.permutations(inputArray))
    
    # Length of iterable, see for discussion of different approaches
    # https://gist.github.com/NelsonMinar/90212fbbfc6465c8e263341b86aa01a8
    permLength = len(allPermutations) 
    #print(permLength)
    
    # Make list of all permutations checks
    results = [True] * permLength 
    pIndex = 0 
    
    # Check all permutations of the input
    for pList in allPermutations:
        # Check all elements of the permutation
        for i in range(len(pList)-1):
            # Compare element to its successor
            if noDifferenceByOneCharacter(pList[i], pList[i+1]):
                results[pIndex] = False
        
        pIndex += 1
    
    #print(results)
    return True in results
                     
# Check whether two strings do not differ by exactly one char
def noDifferenceByOneCharacter(string1, string2):
    counter = 0
    # Task guarantees equal-length strings
    for i in range(len(string1)):
        # Count the character differences
        if string1[i] != string2[i]:
            counter += 1
    
    return False if counter == 1 else True
