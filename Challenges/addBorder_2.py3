# https://app.codesignal.com/challenge/kozrL9G9TzWwWpneJ
# Solution by duckalisk
def addBorder(p):
    s = '*'
    a = [s*len(p[0])]
    
    return [s + r + s for r in a + p + a]