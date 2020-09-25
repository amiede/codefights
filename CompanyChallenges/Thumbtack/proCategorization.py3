# https://app.codesignal.com/company-challenges/thumbtack/ctLXa98xZc3YYGXet
def proCategorization(pros, preferences):
   
    # Categorize
    resultD = dict()
    for i, e in enumerate(preferences):
        for p in preferences[i]:
            if p not in resultD:
                resultD[p] = []
            resultD[p].append(pros[i])
           
    # Make output
    result = []
    for key in sorted(resultD):
        result.append([[key], resultD[key]])
            
    return(result)
      