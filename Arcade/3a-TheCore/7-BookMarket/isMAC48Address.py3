# https://app.codesignal.com/arcade/code-arcade/book-market/HJ2thsvjL25iCvvdm
# https://codefights.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm
def isMAC48Address(inputString):
    return bool(re.match("^([\dA-F]{2}-){5}[\dA-F]{2}$", inputString))
# https://www.regextester.com/