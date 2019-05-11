# Uber Bot: 
def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    
    # Output has same size as input arrays/lists
    fareEstd = [0.0] * len(cost_per_minute)

	# Do the math and round correctly
    for i in range(len(cost_per_minute)):
        currentFare = cost_per_minute[i]*ride_time + cost_per_mile[i]*ride_distance
        fareEstd[i] = round(currentFare, 2)
    
    return fareEstd