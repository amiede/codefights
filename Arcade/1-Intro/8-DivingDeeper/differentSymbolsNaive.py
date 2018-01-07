# https://codefights.com/arcade/intro/level-8/8N7p3MqzGQg5vFJfZ/
def differentSymbolsNaive(string):
    uniqueChars = []
        
    for char in string:
        if not char in uniqueChars:
            uniqueChars.append(char)
            #print(results)
            
    return len(uniqueChars)
