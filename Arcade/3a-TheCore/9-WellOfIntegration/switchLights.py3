# https://app.codesignal.com/arcade/code-arcade/well-of-integration/x3ix7CY93z2bwKDtG
def switchLights(a):
    
    result = [0] * len(a)
    switch = True
    
    for i in range(len(a) - 1, -1, -1):
        
        if a[i] == 1:
            switch = not switch
            
        if switch:
            result[i] = a[i]
        else:
            result[i] = 1^a[i] # flip (or 1-a[i])

    return result
	
'''
# Solution by gavin_patient
def switchLights(a):
    flips = 0
    for i in range(len(a)-1,-1,-1):
        if a[i]==1:
            flips +=1
        a[i] = (a[i]+flips)%2
    return a
	
# Solution by xlxr
def switchLights(a):
    for i in range(len(a)):
        if a[i]:
            for j in range(i+1):
                a[j]=1-a[j]
    return a

'''