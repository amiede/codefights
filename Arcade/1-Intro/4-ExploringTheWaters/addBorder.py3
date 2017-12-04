# https://codefights.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
def addBorder(picture):
   
    newPicture = ["*" * (len(picture[0]) + 2)]
    
    for row in picture:
        newPicture.append("*" + row + "*")
        
    newPicture.append(newPicture[0])
        
    return newPicture