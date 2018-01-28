# https://codefights.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX/
def deleteDigit(n):
    # Generate all possibilities for digit removal
    # This is not expensive as 10 <= n <= 10^6 (7 digits)
    removedDigs = []
    for i in range(len(str(n))):
        value = str(n)[:i] + str(n)[i+1:] # slicing <3
        removedDigs.append(int(value))
    
    # ...and pick the highest one
    return max(removedDigs)