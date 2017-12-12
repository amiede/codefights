# https://codefights.com/challenge/AvdPWyJyixSRdGaYb/
def theJanitor(w):
    l=[] 
    for c in string.ascii_lowercase:
        if c in w:
            l.append(w.rfind(c)-w.find(c)+1)
        else:
            l.append(0)
    return l