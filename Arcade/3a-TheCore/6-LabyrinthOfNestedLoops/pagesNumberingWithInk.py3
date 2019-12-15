# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pdw3izd7SpMTBJqSy
# # https://app.codesignal.com/challenge/xDgfotwk4owqaGyTb
def pagesNumberingWithInk(c, n):

    i = -1
    j = c

    while True:

        n -= len(str(j))

        if n < 0:
            break 

        j += 1
        i += 1          

    return c + i
