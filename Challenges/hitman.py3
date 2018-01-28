# https://codefights.com/challenge/Pbt5rHp85NqPkLm4y
import collections
#p, = eval(dir()[0])
def hitman(p):
    d = collections.deque(p)
    
    while(len(d)>1):
        d.popleft()
        d.append(d.popleft())

    return d.pop()