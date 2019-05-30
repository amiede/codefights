# https://app.codesignal.com/challenge/3GuhySk5idaknKGyY
def directionOfReading(N):

        R = []
        T = []
        l = len(N)
        
        for i in N:
                T.append(("0" * l + str(i))[-l:])
                               
        for i in range(l):
                R.append(int("".join(x[i] for x in T)))
        
        return R