# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/7jaup9HprdJno2diw
def tennisSet(s1, s2):
    
    if max(s1, s2) == 6 and abs(s1-s2) > 1:
        return True
    elif max(s1, s2) == 7 and min(s1,s2) in (5,6):
        return True
    
    return False