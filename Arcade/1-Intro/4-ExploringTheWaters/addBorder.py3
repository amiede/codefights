# https://codefights.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example: For 
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''
def addBorder(picture):
   
    newPicture = ["*" * (len(picture[0]) + 2)]
    
    for row in picture:
        newPicture.append("*" + row + "*")
        
    newPicture.append(newPicture[0])
        
    return newPicture