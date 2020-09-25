# https://codefights.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP
# https://app.codesignal.com/arcade/code-arcade/well-of-integration/xYXfzQmnhBvEKJwXP
def areSimilar(a, b):
    
    diffCounter = 0
    
    # Fail, if there are more than two differences
    for i in range(len(a)):
        if a[i] != b[i]:
            diffCounter += 1
        if diffCounter > 2:
            return False
    
    # 2 or less differences and equal after sort
    # --> Can be re-arranged with 1 swap (of two elements)
    if sorted(a) == sorted(b):
        return True
    
    return False