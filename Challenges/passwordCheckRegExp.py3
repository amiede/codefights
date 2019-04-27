# https://app.codesignal.com/challenge/LpN6NK7cyQmzFukC5
def passwordCheckRegExp(i):
    if re.search(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{5,}", i):
        return True
    
    return False