# https://app.codesignal.com/challenge/8ezof2mziSN8ZbS9C
# Solution by duckalisk
#def splitAddress(a):
splitAddress = lambda a: re.findall('/(\w+)', '/' + a)