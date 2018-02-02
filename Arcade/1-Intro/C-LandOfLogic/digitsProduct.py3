# https://codefights.com/arcade/intro/level-12/NJJhENpgheFRQbPRA
def digitsProduct(product):
    for i in range(1,9999):
        if digitProduct(i) == product:
            return i
    return -1

def digitProduct(n):
    digitList = numberToDigits(n)
    product = 1
    for d in digitList:
        product *= d
    return product
    
def numberToDigits(n):
    return [ int(i) for i in str(n) ]