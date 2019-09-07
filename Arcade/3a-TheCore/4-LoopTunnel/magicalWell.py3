# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LbuWRHnMoJH9SAo4o
def magicalWell(a, b, n):
    
    m = 0
    
    for i in range(n):
        m += a * b
        a += 1
        b += 1
   
    return m  