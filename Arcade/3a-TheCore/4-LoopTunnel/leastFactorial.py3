# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/7BFPq6TpsNjzgcpXy
def leastFactorial(n):

    t = i = 1
       
    while (t < n):
        i += 1
        t *= i
    
    return t