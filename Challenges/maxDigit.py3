# https://app.codesignal.com/challenge/kKTpyheNfKzgfR2nt
def maxDigit(n):
    return max([ int(i) for i in str(n) ])
    #return max(list(map(int, str(n))))
	
# Solution by winstonsmith
# maxDigit = lambda n: int(max(str(n)))