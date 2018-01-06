# https://codefights.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW
def evenDigitsOnly(n):
    digits = [ int(i) for i in str(n) ]

    for d in digits:
        if d % 2 != 0:
            return False
    
    return True