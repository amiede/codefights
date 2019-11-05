# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LAKReA3CR9EwkZGSz
# Solution by bandorthild
def candles(candlesNumber, makeNew):
    return candlesNumber + (candlesNumber - 1) // (makeNew - 1)