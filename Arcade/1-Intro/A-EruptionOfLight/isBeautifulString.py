# https://codefights.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE/
# andrew_pudge's solution for studying
def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    return r[::-1] == sorted(r)