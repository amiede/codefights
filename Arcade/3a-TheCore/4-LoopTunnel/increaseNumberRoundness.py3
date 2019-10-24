# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/KLbRMcWhaZi3dvYH5
def increaseNumberRoundness(n):
    # THE WAY OF THE STRING II
    n = [ int(i) for i in str(n)[::-1] ]

    marker = False
    
    for i in n:
        if i != 0: # we found a non-zero digit
            marker = True
        
        # there is zero digit left of a non-zero digit
        # --> "roundness" can be increased
        if marker == True and i == 0:
            return True
    
    return False