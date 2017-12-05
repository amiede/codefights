# https://codefights.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example
For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.
We can rearrange "aabb" to make "abba", which is a palindrome.
'''
def palindromeRearranging(inputString):
    counter = 0
    symbol = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    for key in symbol:
        if inputString.count(key) % 2 != 0:
            counter += 1
        if counter > 1:
            return False
    
    return True