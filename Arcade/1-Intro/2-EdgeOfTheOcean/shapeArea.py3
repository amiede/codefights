# https://codefights.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ/
def shapeArea(n):
    
    area = 1;
    
    for i in range(1,n):
        area += (i*4)
        
    return area