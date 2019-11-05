# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/3LmZafR9wMCWpdgra
def isSmooth(arr):
    l = len(arr)
       
    if l % 2 == 0:
        m = arr[l//2-1] + arr[l//2]

    else:
        m = arr[l//2]
        
    return m == arr[0] and m == arr[-1]