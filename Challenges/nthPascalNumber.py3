# https://codefights.com/challenge/kP5SCb8NRn7vX9636
def nthPascalNumber(n):
    pTri=[1]
    flatTri=[]
    # Precalculation and flat list of triangle
    for i in range(24): # Gauss: 300 = (24^2 + 24) / 2
        nTri=[]
        flatTri.extend(pTri)
        nTri.append(pTri[0])
        for i in range(len(pTri)-1):
            nTri.append(pTri[i]+pTri[i+1])
        nTri.append(pTri[-1])
        pTri=nTri
     
    return flatTri[n-1]