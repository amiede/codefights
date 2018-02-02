# Uber Bot: 
def fancyRide(l, fares):

    # :-)
    uberOptions = [ "UberX", "UberXL", "UberPlus", "UberBlack" , "UberSUV" ]
    myBudget = 20.0
    
    for i in range(len(fares)):
        # "It is guaranteed that you can afford at least one of them"
        if (l * fares[i]) <= myBudget:
            bestDeal = uberOptions[i]
        
    return bestDeal