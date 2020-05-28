# https://app.codesignal.com/challenge/jTcYipCF76HyCPDSA
#def firstNotRepeatingCharacter(s):
# Solution by notch
# 65
s, = eval(dir()[0])
for i in s:
    if s.find(i) == s.rfind(i):
        return i
return "_"