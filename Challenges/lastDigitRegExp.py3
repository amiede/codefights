# https://app.codesignal.com/challenge/i7XejhS888nXv9pnP
#def lastDigitRegExp(inputString):
return re.search(r'(\d)(?!.*\d)', *eval(dir()[0])).group(0)
# (\d) --> one digit
# (?!.*\d) --> negative look-ahead


# Solution by meadow
#return re.findall('\d',f'{vars()}')[-1]


# Solutions by sil1
#
#return re.sub('\D','',str(vars()))[-1]

# 38 chars
# return re.findall('\d',str(vars()))[-1]

# 42 chars
# return re.findall('\d',*eval(dir()[0]))[-1]