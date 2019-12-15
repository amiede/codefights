# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/MvX84CA5HN6GKqv7R
def squareDigitsSequence(a0):
    
    seen = [ a0 ]
    
    while True:
        
        tsum = 0
        
        for c in str(seen[-1]):
            tsum += int(c)**2
        
        #print(seen)
        
        if tsum in seen:
            return len(seen) + 1
        else:
            seen += [ tsum ]
    