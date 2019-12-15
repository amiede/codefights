# https://app.codesignal.com/challenge/nzDQW93qQgYNGJK46
#def fractionReducing(fraction):
N, = eval(dir()[0])
g = numpy.gcd(N[0], N[1])
return (N[0] // g, N[1] // g)