# https://codefights.com/challenge/KoHhZRuN38QpfKfsX
# ===================================================
# source => count non-zero bits, this is the number 
# of zero bits to be flipped in "target" (from right)
# ===================================================
# [int(i) for i in bin(t)[:1:-1]]
# => convert "t" to binary and reverse order
# (because bits are changed from the right)
# ===================================================
def binateNilFill(s, t):
    r = []
    c = 0     
    for b in [int(i) for i in bin(t)[:1:-1]]:
        a = b 
        if ((b == 0) and (c < bin(s).count("1"))): 
            a = 1
            c += 1
        r.insert(0, a)
    
    return int(''.join(map(str,r)),2)