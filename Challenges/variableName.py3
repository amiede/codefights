# https://app.codesignal.com/challenge/XRkmdi6TzMx5AsDuv
#def variableName(name):
#n, = eval(dir()[0])
return True if re.search(r"^[a-zA-Z_]\w*$", *eval(dir()[0])) else False
# ^$ Start/end of line
# [a-zA-Z_] Start with one letter/underscore
# \w* Then 0 or more alphanumeric characters


# Solutions by aeiou
#
#variableName = lambda s: re.search(r'^\d|\W', s) is None

# 51
# s, = eval(dir()[0])
# return re.search(r'^\d|\W', s) is None