# https://app.codesignal.com/challenge/ddEZp78usMvhQEu3i
#def arrayConversion(inputArray):
# 132
A, = eval(dir()[0])
i = 0

while len(A) != 1:
    i += 1
    
    if i % 2 == 0:
        o = "*"
    else:
        o = "+"
        
    A = [ eval("%s%s%s" % (a, o, b)) for a, b in zip(A[0::2], A[1::2]) ]

return A[0]


# 133
#A, = eval(dir()[0])
#i = 0
#
#while len(A) != 1:
#    i += 1
#    
#    if i % 2 == 0:
#        A = [ a * b for a, b in zip(A[0::2], A[1::2]) ]
#    else:
#        A = [ a + b for a, b in zip(A[0::2], A[1::2]) ]
#
#return A[0]