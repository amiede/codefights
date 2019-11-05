# https://app.codesignal.com/challenge/EbMqajTbSWmhTcpoQ
# Solution by nullie
#def unusualDictionary(wordList):
f = [(w.split()[-1], w) for w in eval(dir()[0])[0]]
return f == sorted(f)

# 63
# l, = eval(dir()[0])
# f = [(w.split()[-1], w) for w in l]
# return f == sorted(f)

# 65
# l, = eval(dir()[0])
# return l == sorted(l, key=lambda w: (w.split()[-1], w))

# 72
# l, = eval(dir()[0])
# return l == sorted(l, key=lambda w: (re.sub('^\w+ ', '', w), w))

# 84
# p = ()
# for w in eval(dir()[0])[0]:
#     d = (re.sub('^\w+ ', '', w), w)
#     if d < p:
#         return False
#     p = d
# return True

# 81
# l, = eval(dir()[0])
# return l == sorted(l, key=lambda w: (re.sub('^(to|the|an?) ', '', w), w))