#def VedicTwoDigitMultiplication(a, b):
a,b = eval(dir()[0])
da = [ int(i) for i in str(a) ]
db = [ int(i) for i in str(b) ]
return [ da[0] * db[0], da[0] * db[1] + da[1] * db[0] , da[1] * db[1] ]