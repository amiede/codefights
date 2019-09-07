# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/whz5JzszYTdXW6aNA
def differentRightmostBit(n, m):
    return (n ^ m) & -(n ^ m)