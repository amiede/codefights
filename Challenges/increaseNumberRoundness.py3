# https://app.codesignal.com/challenge/9JMQovWr4cZ933o6S
#def increaseNumberRoundness(n):
return '0' in str(*eval(dir()[0])).rstrip('0')


# Solutions by nullie
#
#return '0' in str(vars())[:-16].strip('0')

# 41
# return re.findall('0[1-9]', str(vars())) > []

# 63
# increaseNumberRoundness = f = lambda n: n > 100 and (0 < n % 100 < 10 or f(n / 10))