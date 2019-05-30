# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/eC2Zxu5H5SnuKxvPT/
def rangeBitCount(a, b):
    return sum( bin(i).count("1") for i in range(a, b+1))