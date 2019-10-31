# https://app.codesignal.com/challenge/osJK8YhviaN5bQT5m
#def isGeometricProgression(sequence):
s, = eval(dir()[0])
f = s[1]/s[0]

for i in range(1,len(s)): 
    # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    if abs(s[i-1]*f - s[i]) > 1e-6:
            return False
    
return True