
# https://app.codesignal.com/challenge/2NK7BGPbWb5FDWJ59
# "2 apples, 12 oranges" --> 2 + 1 + 2 = 5
#def sumUpDigits(inputString):
# 53
sumUpDigits = lambda s: sum(map(int, re.findall(r'\d', s))) 

# 53
#sumUpDigits = lambda s: sum([ int(c) for c in s if c.isdigit() ])

# 56
#s, = eval(dir()[0])
#return sum([ int(c) for c in s if c.isdigit() ])

# 57
#sumUpDigits = lambda s: sum(map(int, [ c for c in s if c.isdigit() ] ))

# 59
#sumUpDigits = lambda s: sum(map(int, filter(unicode.isdigit, s)))

# Note:
# Use str.split() or \d+ (regex) if not single digits but 
# numbers were required, e.g. 
# "2 apples, 12 oranges" --> 2 + 12 = 14


# Solutions by sil1
# 45
return sum(int(x) for x in str(vars()) if '/'<x<':')
# 48 chars
# return sum(map(int,re.findall('\d',str(vars()))))