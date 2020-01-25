# https://app.codesignal.com/challenge/zBDDWvf2sHC7d3Dok
#def shuffledArray(shuffled):
# 82 
S, = eval(dir()[0])
for i in range(len(S)):
    T = S[:i] + S[i+1:]
    if S[i] == sum(T):
        return sorted(T)
		
		
# Solution by synth
# 50		
#A, = eval(dir()[0])
#A.remove(sum(A)/2)
#return sorted(A)