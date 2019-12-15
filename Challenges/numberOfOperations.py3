# https://app.codesignal.com/challenge/Zwx3cM3w543cC3sDP
#def numberOfOperations(a, b):
a, b = eval(dir()[0])
N = sorted([a, b])
c = 0

while N[1] % N[0] == 0:
    N[1] = N[1] / N[0]
    N.sort()
    c += 1

return c