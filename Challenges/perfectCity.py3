# https://app.codesignal.com/challenge/fRpCbgbt38t3RKg2q
# Uber Bot
#def perfectCity(a, b):
a, b = eval(dir()[0])
f = math.floor
d = 0

# Iterate over all coordinates (generic for more dimensions ;-)
for i in range(len(a)):
    # Base case: not in same block
    if f(a[i]) != f(b[i]):
        # Calculate "plain" d
        d += abs(a[i] - b[i])
    
    # Challenge case: in same block
    else:
        # Sum of each d to corner
        x = a[i] - f(a[i]) + b[i] - f(b[i])
        
        # > 1 would not be the shortest route
        d = d + x if x < 1 else d + 2 - x
        
return d