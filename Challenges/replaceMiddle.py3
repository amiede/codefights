# https://app.codesignal.com/challenge/yevt2AXgvguitTzzu
#def replaceMiddle(a):
a, = eval(dir()[0])

l = len(a)

if l % 2 == 0:
    l //= 2
    a[l] = a[l] + a[l-1]
    a.pop(l-1)

return a

