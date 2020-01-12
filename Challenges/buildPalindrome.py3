# https://app.codesignal.com/challenge/Fucm34ZryB8EBKbJP
# https://codefights.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx
#def buildPalindrome(s):
s, = eval(dir()[0])
# Is already a Palindrome?
if s == s[::-1]:
    return s

# Add the (reversed) first part of the original at the end
for i in range(len(s)):
    n = s + s[0:i+1][::-1]
    if n == n[::-1]:
        return n
		
		
# Solution by duckalisk
#s, = eval(dir()[0])
#
#t = ''
#for c in s:
#    q = s + t
#    if q == q[::-1]:
#        return q
#    t = c + t		