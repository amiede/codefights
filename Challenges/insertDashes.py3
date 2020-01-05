# https://app.codesignal.com/challenge/PLyDoCvsWjCNpSFux
#def insertDashes(i):
# Bad Friday-afternoon solution :-\
# 91
i, = eval(dir()[0])
r = ""
for c, d in zip(i, i[1:]):
    if " " not in {c, d}:
        x = "-" 
    else: 
        x = ""
    r += c + x

return r + i[-1]


# 38
# Solution by duckalisk
# assumes single spaces only
return re.sub('\B', '-', *eval(dir()[0]))