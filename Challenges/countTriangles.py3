# https://app.codesignal.com/challenge/hbRLsbDh9fTSFapAB
# https://www.geeksforgeeks.org/number-possible-triangles-cartesian-coordinate-system/
def countTriangles(x, y):    
    
    l = len(x)
    r = 0
    
    for i in range(l): 
        for j in range(i + 1, l): 
            for k in range(j + 1, l):    
                # Determinant of three points --> area of that triangle
                d = x[i] * (y[j] - y[k]) - y[i] * (x[j] - x[k]) + 1 * (x[j] * y[k] - y[j] * x[k])
                # No area, no triangle
                if d != 0: r += 1
  
    return r