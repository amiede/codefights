# https://codefights.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
# Bought hint from pharfenmeister (thx!)
# Reconstructed solution :-\
def almostIncreasingSequence(sequence):
    
    # Boolean for checking whether we 
    # already removed one element
    removedOne = False

    # Be lower than the minimum of the list
    last = min(sequence) - 1 
    prev = last 
    
    # Iterate over list
    for currentNumber in sequence:
        #print(currentNumber, last, prev)
        # Sequence is not increasing
        if currentNumber <= last:
            if removedOne: 
                # Second time to remove smth.
                # --> FAIL
                return False
            else:
                # First time to remove smth.
                # --> Still OK
                removedOne = True
            if currentNumber < prev:
                # "Remove" currentNumber from list
                prev = last
            elif currentNumber > prev:
                # "Remove" last number from list
                prev = last = currentNumber
        else:
            # Move forward in list
            prev = last
            last = currentNumber
    return True