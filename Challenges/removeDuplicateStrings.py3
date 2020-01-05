# https://app.codesignal.com/challenge/pC6LK4Ne2jHjP74Ew
#def removeDuplicateStrings(inputArray):

# 49    
I, = eval(dir()[0])    
return sorted(set(I), key=I.index)

# 49
#return list(dict.fromkeys(*eval(dir()[0])).keys())

# 61
#I, = eval(dir()[0])    
#x = set()
#return [ i for i in I if not (i in x or x.add(i)) ]