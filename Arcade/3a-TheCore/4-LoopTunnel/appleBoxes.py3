# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/scG8AFsPuqQGx8Qjf
def appleBoxes(k):
    
    red = yellow = 0
    
    for i in range(1, k+1):
        if i % 2:
            yellow += i**2
        else:
            red += i**2
            
    return red - yellow