# https://app.codesignal.com/challenge/4TDbzaLfpySTBmCuF
#def equationSolutions(l, r):
l,r = eval(dir()[0])
R = []
for a in range(l, r+1):
    for b in range(l, r+1):
        if a**3 == b**2:
            #R.append((a,b)) # functionally correct
            R.append(a) # short version for task
return len(R)