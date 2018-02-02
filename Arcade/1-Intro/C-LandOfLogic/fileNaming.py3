# https://codefights.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC
def fileNaming(names):
    
    # Result after the renaming
    newNames = [] 
    
    # Keep track of the already-used file names
    uniqueNames = {}
   
    # Check all file names
    for n in names:
        tempName = n
        counter = 1
        
        # Adjust the file name if it is already used
        while tempName in uniqueNames:
            tempName = n + "(" + str(counter) + ")"
            counter += 1
            #print(tempName)
        
        uniqueNames[tempName] = True # Mark as see
        newNames.append(tempName) # Add to result
    
    return newNames