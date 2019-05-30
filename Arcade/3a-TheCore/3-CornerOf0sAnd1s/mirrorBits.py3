# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/e3zfPNTwTa9qTQzcX
def mirrorBits(a):
     # int --> bin (reverse like string and cut "0b") --> int
     return int(bin(a)[:1:-1],2)