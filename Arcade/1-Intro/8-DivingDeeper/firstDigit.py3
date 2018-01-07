# https://codefights.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov
def firstDigit(inputString):
    # See https://pythex.org/ for some testing
    matches = re.search(r"\d", inputString)
    return matches.group(0) # first match