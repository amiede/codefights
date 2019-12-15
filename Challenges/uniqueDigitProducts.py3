# https://app.codesignal.com/challenge/rcTSmoy6pRx7frN4y
#def uniqueDigitProducts(a):
a, = eval(dir()[0])
S = set()
for x in a:
    # Convert each int in list to digits list
    # Calculate product of digits (via numpy)
    # Add to set to have unique products
    S.add(numpy.prod([ int(i) for i in str(x) ]))

return len(S)