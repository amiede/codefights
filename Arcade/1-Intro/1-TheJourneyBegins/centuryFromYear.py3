# https://codefights.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
def centuryFromYear(year):
# Old, clumsy solution
temp = year / 100
    if temp - int(temp) > 0:
        return int(temp) + 1
    else:
        return int(temp)