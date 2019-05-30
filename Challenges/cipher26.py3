# https://app.codesignal.com/challenge/9MpWuqH25gnxNHnvC
def cipher26(m):

    r = ""
    a = 0
    
    for c in m:
        r += chr((ord(c) - 97 - a) % 26 + 97) 
        a = ord(c) - 97
    
    return r