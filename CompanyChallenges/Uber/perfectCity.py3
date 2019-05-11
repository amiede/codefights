# Uber Bot
def perfectCity(departure, destination):

    distance = 0
    
    # Iterate over all coordinates (generic for more dimensions ;-)
    for i in range(len(departure)):
        # Base case: not in same block
        if (math.floor(departure[i]) != math.floor(destination[i])):
            # Calculate "plain" distance
            distance += abs(departure[i] - destination[i])
        
        # Challenge case: in same block
        else:
            # Sum of each distance to corner
            blockDiff = (departure[i] - math.floor(departure[i])) + (destination[i] - math.floor(destination[i]))
            
			# Check for route being too long
            if blockDiff < 1: # OK, shortest
                distance += blockDiff
            else: # > 1 would not be the shortest route
                distance += 2 - blockDiff
            
    return distance