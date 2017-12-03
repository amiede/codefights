# https://codefights.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
def commonCharacterCount(s1, s2):
    
    # Unique common characters (not asked :-( )
    #return(len(set(s1) & set(s2)))
    
    counter = 0
    
    # Check only the intersecting characters
    for char in (set(s1) & set(s2)):
        # Minimum number of common occurrences (per task descr.)
        counter += min(s1.count(char), s2.count(char))
    
    return counter