# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/8rqs3BLpdKePhouQM
def lineUp(c):

    if c == "" or c == "R" or c == "L":
        return 0
    elif c == "A":
        return 1
    else:
        count = 0
        face = True
        
        for i in c:
            if i == "R" or i == "L":
                if face == False:
                    count += 1
                    face = True
                else:
                    face = False
            if i == "A" and face == True:
                count += 1
                
        return count
