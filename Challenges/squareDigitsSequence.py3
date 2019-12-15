# https://app.codesignal.com/challenge/YPAhD7Tz3o3E4vwBi
# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/MvX84CA5HN6GKqv7R
#def squareDigitsSequence(a0):
s = eval(dir()[0])
while True:
    t = 0
    for c in str(s[-1]):
        t += int(c)**2
    if t in s:
        return len(s) + 1
    else:
        s += [ t ]