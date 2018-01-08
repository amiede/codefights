# https://codefights.com/arcade/intro/level-9/xHvruDnQCx7mYom3T
def growingPlant(upSpeed, downSpeed, desiredHeight):
    day = 0
    height = 0
    
    while True:
        height += upSpeed # day
        day += 1
        if height >= desiredHeight:
            return day
        height -= downSpeed # night