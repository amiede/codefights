# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LAKReA3CR9EwkZGSz
def candles(candlesNumber, makeNew):
   
    burnSum = 0
    leftovers = 0
    
    while candlesNumber > 0:
        burnSum += candlesNumber 
        leftovers += candlesNumber 
        candlesNumber = 0
        candlesNumber += leftovers // makeNew
        leftovers -= candlesNumber * makeNew
               
    return burnSum