# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/H5PP5MXvYvWXxTytH
def rounders(n):
    if n <= 9:
        return n
    
    elif n % 10 >= 5:
        return rounders(n / 10 + 1) * 10
        
    else:
        return rounders(n / 10) * 10