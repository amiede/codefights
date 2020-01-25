# https://app.codesignal.com/arcade/code-arcade/book-market/MX94DWTrwQw2gLrTi
#def htmlEndTagByStartTag(startTag):
def htmlEndTagByStartTag(s):
    s = re.search("<[^\s/>]+", s).group() 
    return s[0] + "/" + s[1:] + ">" 