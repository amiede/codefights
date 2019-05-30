# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/eC2Zxu5H5SnuKxvPT
def rangeBitCount(a, b):
    
    sum = 0
    
    for i in range(a,b+1):
        sum += bin(i).count("1")

    return sum