# https://app.codesignal.com/challenge/kozrL9G9TzWwWpneJ
# https://codefights.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
#def addBorder(picture):
p, = eval(dir()[0])
x = "*" 
n = [ x * (len(p[0]) + 2) ]

for r in p:
    n += [ x + r + x ]

n += [ n[0] ]

return n