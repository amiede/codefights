# https://app.codesignal.com/challenge/xDgfotwk4owqaGyTb
#def pagesNumberingWithInk(c, n):
c,n = eval(dir()[0])

i = -1
j = c

while True:

    n -= len(str(j))

    if n < 0:
        break 

    j += 1
    i += 1          

return c + i