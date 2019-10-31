# https://app.codesignal.com/challenge/TieSbaDHnbGyKjfKa
#def digitDistanceNumber(n):
n = [ int(i) for i in str(*eval(dir()[0])) ]
   
r = [ abs(n[i+1] - n[i]) for i in range(len(n)-1) ]
    
return int(''.join((map(str, r))))