# https://app.codesignal.com/challenge/hiPeCwLgendpQASyD
def isPower(n):
    if n == 1: return True 
    for i in range(2, int(n**0.5) + 1) : 
        x = i 
  
        while x <= n: 
            x = x * i 
              
            if x == n: 
                return True
    
    return False
	

# Solution by synth
# r = range
# isPower = lambda n: n in [a**b for a in r(n) for b in r(n)]