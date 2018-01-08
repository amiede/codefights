# https://codefights.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo
# Thanks to christoph558 for his comment on "distance check"
def bishopAndPawn(bishop, pawn):
    # Bishop moves diagonally
    # So distance X must be same 
    distX = ord(bishop[0]) - ord(pawn[0])
    # as distance Y (btw. Bishop/Pawn)
    distY = int(bishop[1]) - int(pawn[1])
    
    return abs(distX) == abs(distY)
    
    #print(ord(bishop[0]), ord(pawn[0]))
    #print(int(bishop[1]), int(pawn[1]))