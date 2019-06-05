# https://app.codesignal.com/challenge/Fucm34ZryB8EBKbJP
#def buildPalindrome(s):
# Solution by duckalisk
s, = eval(dir()[0])

t = ''
for c in s:
    q = s + t
    if q == q[::-1]:
        return q
    t = c + t