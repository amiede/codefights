# https://codefights.com/challenge/nqQFNy2QTJsHyMBZG
def hasPairWithSum(array, number):
    
    # Brute-force solution ;-)
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[i]+array[j] == number:
                return True
    
    return False