# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/b5z4P2r2CGCtf8HCR
def killKthBit(n, k):
    return n & ~2**(k-1) 