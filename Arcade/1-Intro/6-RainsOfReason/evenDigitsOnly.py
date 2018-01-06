# https://codefights.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW/
def evenDigitsOnly(n):
    return ( sum( [ int(i) % 2 for i in str(n) ] ) == 0 )