# https://app.codesignal.com/challenge/K3J68NkFj5Tbi8tJR
# Solution by denniscomella
# def lookAndSaySequenceNextElement(e):
return ''.join(str(len(b)+1)+a  for a,b in re.findall(r'(.)(\1*)', eval(dir()[0])[0]))

# def lookAndSaySequenceNextElement(element):
#     return ''.join(str(len(b)+1)+a  for a,b in re.findall(r'(.)(\1*)',element))


## see also: lineEncoding() -> https://app.codesignal.com/challenge/wBBHdf8aSNd4q9ECZ