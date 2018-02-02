# https://codefights.com/arcade/intro/level-12/YqZwMJguZBY7Hz84T
def sumUpNumbers(inputString):
    
    # Find all numbers (multiple digits) and convert from string to int list
    numbers = [ int(i) for i in re.findall(r'\d+', inputString) ]
     
    return sum(numbers)