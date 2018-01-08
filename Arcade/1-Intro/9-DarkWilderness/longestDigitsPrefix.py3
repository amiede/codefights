# https://codefights.com/arcade/intro/level-9/AACpNbZANCkhHWNs3
def longestDigitsPrefix(inputString):
    # See https://pythex.org/ for some testing
    matches = re.match(r"^(\d)+", inputString)
    if matches:
        return matches.group(0)
    else:
        return ""