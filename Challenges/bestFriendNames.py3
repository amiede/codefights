# https://codefights.com/challenge/RTHN8Lgek9PTyPRBX
def bestFriendNames(n, m):
    return (fs(n) == fs(m))
    
def fs(n):    
    fs = 0
    for c in n:
        if c != " ": 
			fs += ord(c.lower()) - 96
    return fs   