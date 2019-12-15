# https://app.codesignal.com/challenge/i7XejhS888nXv9pnP
#def lastDigitRegExp(inputString):
return re.search(r'(\d)(?!.*\d)', *eval(dir()[0])).group(0)
# (\d) --> one digit
# (?!.*\d) --> negative look-ahead