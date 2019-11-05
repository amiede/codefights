# https://app.codesignal.com/challenge/XRkmdi6TzMx5AsDuv
# Solution by aeiou
#def variableName(name):
variableName = lambda s: re.search(r'^\d|\W', s) is None

# 51
# s, = eval(dir()[0])
# return re.search(r'^\d|\W', s) is None