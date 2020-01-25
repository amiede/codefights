# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/tuKA5f3zpzkKKejJx/
# Thanks for the helpful comments
def rectangleRotation(a, b):
    x = math.ceil(a / 2**0.5)
    y = math.ceil(b / 2**0.5)
    
    t = (x * y) + ( (x - 1) * (y - 1) )
    
    return t if t % 2 != 0 else t - 1 