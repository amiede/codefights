# https://codefights.com/arcade/python-arcade/slithering-in-strings/GADdmPKQivSzQGYLw
def newStyleFormatting(s):
    placeHolder = "{{"
    s = s.replace("%%",placeHolder)
    s = re.sub(r'%[a-z]',"{}", s)
    s = s.replace(placeHolder,"%")
    return s
