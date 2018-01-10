# https://codefights.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx
def buildPalindrome(st):
    # Is already a Palindrome?
    if st == st[::-1]:
        return st
    
    # Add the (reversed) first part of the original at the end
    for i in range(len(st)):
        newSt = st + st[0:i+1][::-1]
        if newSt == newSt[::-1]:
            return newSt