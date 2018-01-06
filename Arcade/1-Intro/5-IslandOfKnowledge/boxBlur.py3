# https://codefights.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP
def boxBlur(image):

    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 ( 0, -1), ( 0, 0), ( 0, 1),
                 ( 1, -1), ( 1, 0), ( 1, 1)] 

    rows = len(image)
    cols = len(image[0])
    
    result = []
    
    # Iterate over the core cells
    for i in range(rows-2):
        innerResult = []
        for j in range(cols-2):
            # Calculate sum and avg of all neighbors
            neighborSum = 0
            for f, g in neighbors:
                x = i + 1 + f
                y = j + 1 + g
                neighborSum += image[x][y]
            innerResult.append(math.floor(neighborSum/len(neighbors)))
        result.append(innerResult)
    
    return result