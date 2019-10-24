# https://app.codesignal.com/challenge/m399dDgJDCeQA6jF5
#def deleteDigit(n):
l = [ int(i) for i in str(*eval(dir()[0])) ]
r = []

for i in range(len(l)):
    t = l[:]  # fastest way to copy
    del t[i]
    r.append(int(''.join((map(str, t)))))

return max(r)