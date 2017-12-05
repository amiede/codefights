# https://codefights.com/challenge/JbpJhJYDovKY5TeqK
'''
Given a sentence, check whether it is a pangram or not.

Example
For sentence = "The quick brown fox jumps over the lazy dog.", the output should be
isPangram(sentence) = true;
For sentence = "abcdefghijklmnopqrstuvwxya", the output should be
isPangram(sentence) = false.
'''
def isPangram(sentence):
    plainAlphabet = string.ascii_lowercase 
    
    # check all the letters in the alphabet
    for char in plainAlphabet:
        if char not in sentence.lower(): # against sentence
            return False # isNotPangram

    return True # isPangram