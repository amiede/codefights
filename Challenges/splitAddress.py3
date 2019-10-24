# https://app.codesignal.com/challenge/8ezof2mziSN8ZbS9C
#def splitAddress(a):
a, = eval(dir()[0])
a = a.split("/")
a[0] = a[0][:-1]
a[2] = a[2].split(".")[0]
a.pop(1)   
return a