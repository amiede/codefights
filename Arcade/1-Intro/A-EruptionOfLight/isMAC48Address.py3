# https://codefights.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm
def isMAC48Address(inputString):

    # Check general length of the address and  
    # check correct number of groups
    groups = inputString.split("-")
    if (len(groups) != 6) or (len(inputString) != 17):
        return False
    
    # Hexadecimal conversion with exception
    try:
        for g in groups:
            int(g, 16)
            
        return True
    except ValueError:
        return False
    
    # RegEx solution: ToDo
    # --> r"([0-9a-fA-F]{2}[-]){5}([0-9a-fA-F]{2})"