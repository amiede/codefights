# https://codefights.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m/
def adjacentElementsProduct(inputArray):
    
    product = -sys.maxsize
    
    for i in range(0, len(inputArray)-1):
        current = inputArray[i]
        nextt = inputArray[i+1]
        if current*nextt > product:
            product = current*nextt 
    
    return product