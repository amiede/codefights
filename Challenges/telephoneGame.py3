# https://codefights.com/challenge/6RSivQPsn59o8YQWw
def telephoneGame(m):
    for i in range(0,len(m)-1):
        if m[i] != m[i+1]:
            return i+1
    return -1 