# https://app.codesignal.com/challenge/6CH5C9bcLd9Pfoyk7
#def htmlEndTagByStartTag(startTag):
s, = eval(dir()[0])
s = re.search("<[^\s/>]+", s).group() 
return s[0] + "/" + s[1:] + ">" 


# Solution by winstonsmith
#return '</' + re.findall('\w+',  str(vars()) )[1] + '>'