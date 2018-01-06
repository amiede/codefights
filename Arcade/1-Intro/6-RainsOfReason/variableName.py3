# https://codefights.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
def variableName(name):
    #  str.isidentifier()
    #  Return true if the string is a valid identifier according 
    #  to the language definition, section Identifiers and keywords.
    #  https://docs.python.org/3.7/reference/lexical_analysis.html#identifiers
    #return name.isidentifier()
    
    # RegEx
    # ^ Start of line
    # [a-z_] Start with letter or underscore
    # \w* Then contain 0 or more alphanumerica characters
    # $ End of line
    if re.search(r"^[a-z_]\w*$", name): # return match object
        return True
    else:
        return False