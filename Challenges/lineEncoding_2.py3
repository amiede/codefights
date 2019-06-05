# https://app.codesignal.com/challenge/wBBHdf8aSNd4q9ECZ
# Solution by minhphan
# def lineEncoding(s):
s, = eval(dir()[0])
return re.sub(r"(.)\1+", lambda m: str(len(m.group(0))) + m.group(1), s)