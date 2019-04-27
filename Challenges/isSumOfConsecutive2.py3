# https://app.codesignal.com/challenge/CY2qYcwMqPxp6Rsst
#def isSumOfConsecutive2(n):   
n, = eval(dir()[0])
c = 0

for i in range(1,n):
    s = i
    j = 1

    while s < n:
        s = s + i + j
        j += 1

    if s == n:
        c += 1

return c