# https://app.codesignal.com/arcade/code-arcade/mirror-lake/kGeuCkJNbqczCCqgg
def numbersGrouping(a):

    groups = { math.ceil(e/10**4) for e in a }
           
    return len(groups) + len(a)