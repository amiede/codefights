# https://app.codesignal.com/arcade/code-arcade/well-of-integration/sGwCfM5FzX7LhLcdk/comments
def minimalNumberOfCoins(coins, price):
    nCoins = 0
    
    for coin in coins[::-1]:
        nCoins += price // coin
        price %= coin
    
    return nCoins