# https://codefights.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq
def absoluteValuesSumMinimization(a):
    # Ugly solution, just guessing from looking at the tests
    if len(a) % 2 == 0:
        return a[math.floor(len(a)/2-1)]
    else:
        return a[math.floor(len(a)/2)]
    # Shorter version, of course (andrew_pudge)
    # return a[(len(a)-1)//2] 