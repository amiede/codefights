# https://app.codesignal.com/company-challenges/codesignal/gJMBmTwHHMF8mbQvH
def companyBotStrategy(trainingData):

    summe = 0
    correct = 0

    for d in trainingData:
        if d[1] == 1:
            summe += d[0]
            correct += 1
        
    return summe/correct if correct != 0 else 0