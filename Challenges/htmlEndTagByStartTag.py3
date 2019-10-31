# https://app.codesignal.com/challenge/6CH5C9bcLd9Pfoyk7
#def htmlEndTagByStartTag(startTag):
s, = eval(dir()[0])
s = re.search("<[^\s/>]+", s).group() 
return s[0] + "/" + s[1:] + ">" 