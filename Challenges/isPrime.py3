# https://app.codesignal.com/challenge/rCfCTkrbE4PDE9J2w
def isPrime(n):
#n = eval(dir()[0])

    return all(n % i for i in range(2,n))
    
    # The all() function returns True if all items in an iterable are true, 
    # otherwise it returns False.