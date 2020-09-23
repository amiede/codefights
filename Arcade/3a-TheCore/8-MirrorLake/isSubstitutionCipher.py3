# https://app.codesignal.com/arcade/code-arcade/mirror-lake/rNrF4v5etMdFNKD3s
def isSubstitutionCipher(string1, string2):

    checker = dict()
    
    for i in range(len(string1)): # both have same length
        if string1[i] in checker:
            if checker[string1[i]] != string2[i]:
                return False            
        else:
            # cypher already exists for other key
            if string2[i] in checker.values(): 
                return False
            else:
                checker[string1[i]] = string2[i]
    
    return True    