# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf
# Solution by mathgeek
def arrayPacking(a):
    out = 0
    for i in range(len(a)):
        out += a[i] << 8*i
    return out