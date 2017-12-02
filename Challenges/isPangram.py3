# https://codefights.com/challenge/JbpJhJYDovKY5TeqK
def isPangram(sentence):
    plainAlphabet = "abcdefghijklmnopqrstuvwxyz" # ISO basic Latin alphabet
    
    # check all the letters in the alphabet
    for char in plainAlphabet:
        if char not in sentence.lower(): # against sentence
            return False # isNotPangram

    return True # isPangram