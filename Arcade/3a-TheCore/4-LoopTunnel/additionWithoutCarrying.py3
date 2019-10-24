# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/xzeZqCQjpfDJuN72S
def additionWithoutCarrying(param1, param2):
    # THE STRING WAY ;-)
    # convert int to (reversed) int list
    param1 = [ int(i) for i in str(param1)[::-1] ]
    param2 = [ int(i) for i in str(param2)[::-1] ]
    
    # padding of uneven params
    diff = len(param1) - len(param2)
    
    if diff < 0:
        param1.extend([0] * abs(diff))
    elif diff > 0:
        param2.extend([0] * abs(diff)) 
    
    res = []
    
    for a, b in zip(param1,param2):
        res.append((a+b) % 10)
        
    return int(''.join((map(str, res)))[::-1])