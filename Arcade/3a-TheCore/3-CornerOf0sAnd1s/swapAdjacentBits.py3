# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/dShYZZT4WmvpmfpgB
def swapAdjacentBits(n):
    return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
