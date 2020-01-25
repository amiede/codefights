# https://app.codesignal.com/challenge/ESBdiMSa8YTr95qFx
# letterValue * 26**i,
# where i is the 0-based index 
# of the reversed string
#def excelSheetColumnNumber(s):

# 66
r = i = 0
for e in eval(dir()[0])[0][::-1]:
    r += (ord(e) - 64) * 26**i
    i += 1
return r

# 72
#return sum([ (ord(e) - 64) * 26**i for i, e in enumerate(eval(dir()[0])[0][::-1]) ])

# 73
#r = 0
#for i, e in enumerate(eval(dir()[0])[0][::-1]):
#    r += (ord(e) - 64) * 26**i
#return r


# Solution by itsoes
# 50
#r=0
#for c in eval(dir()[0])[0]:
#    r = r*26 + ord(c)-64
#return r