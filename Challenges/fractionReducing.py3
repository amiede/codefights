# https://app.codesignal.com/challenge/nzDQW93qQgYNGJK46
#def fractionReducing(fraction):
N, = eval(dir()[0])
g = numpy.gcd(N[0], N[1])
return (N[0] // g, N[1] // g)

#Solution by synth
#a, = eval(dir()[0])
#return a/numpy.gcd(*a)

#Solution by raj_l2
#def fractionReducing(f):
#    a,b=f
#    g =math.gcd(a,b)
#	# g = math.gcd(*f)
#   return[a/g,b/g]