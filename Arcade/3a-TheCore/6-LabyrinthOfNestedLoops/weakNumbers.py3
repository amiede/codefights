# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/oL7YuygJKtMSNLeJn
# Thanks to the_mole
# Count factors of a number
def countDivisors(n) : 
    count = 0
    for i in range(1, int(n**0.5) + 1) : 
        if (n % i == 0) : 
            if (n / i == i) : 
                count += 1
            else : 
                count += 2                
    return count 

# Weakness is considered the amount of numbers that 
# come before N which have more divisors than N
def weakNumbers(n):

    divisorsList = []
    weaknesses = []
    
    # Make an array with divisors count
    for i in range(1, n + 1):
        divisorsList.append(countDivisors(i))
    
    # Make an array of weaknesses
    for c, e in enumerate(divisorsList):
        prevElementsWithMoreDivisors = sum( i > e for i in divisorsList[:c] )
        weaknesses.append(prevElementsWithMoreDivisors)
    
    # Highest weakness and how often this occurs
    return [ max(weaknesses), weaknesses.count(max(weaknesses)) ]
    

# Solution by weejie
#X = []
#W = []
#n = 0
#while n<eval(dir()[2])[0]:
#    n += 1
#    x = i = 0
#    while i<n:
#        i += 1
#        x += n%i<1
#
#    X += x,
#    W += sum(x<z for z in X),
#
#w = max(W)
#
#return w, W.count(w)
