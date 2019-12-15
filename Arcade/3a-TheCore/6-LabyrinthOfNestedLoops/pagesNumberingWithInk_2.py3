# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pdw3izd7SpMTBJqSy
# Solution by sfogmoon
def pagesNumberingWithInk(current, numberOfDigits):
    if numberOfDigits < 0:
        return current - 2
    return pagesNumberingWithInk(current+1, numberOfDigits - len(str(current)))