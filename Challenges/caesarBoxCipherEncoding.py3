# https://app.codesignal.com/challenge/bXXQbc5cesH7jPtXr
#def caesarBoxCipherEncoding(inputString):
i, = eval(dir()[0])
n = int(len(i)**0.5)
x = ""

for a in range(n):
    for b in range(0, len(i), n):
        x += i[a+b]

return x