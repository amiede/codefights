# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/yBFfNv5fTqhcacZ7w
def isPower(n):
    if n == 1: return True 
    for i in range(2, int(n**0.5) + 1) : 
        x = i 
  
        while x <= n: 
            x = x * i 
              
            if x == n: 
                return True
    
    return False