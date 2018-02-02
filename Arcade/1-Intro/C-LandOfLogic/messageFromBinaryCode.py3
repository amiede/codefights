# https://codefights.com/arcade/intro/level-12/sCpwzJCyBy2tDSxKW
def messageFromBinaryCode(code):

    stepSize = 8
    resultString = ''
    
    # Step over input code
    for i in range(0, len(code), stepSize):
        # Extract step-sized slice, convert bin to int to char
        resultString += chr(int(code[i:i+stepSize],2))
        
    return resultString