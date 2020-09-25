# https://app.codesignal.com/company-challenges/codesignal/68DxrkM9yXirF4fuD
def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):

    # not solved
    if successfulSubmissionTime == -1:
        return 0
    #elif successfulSubmissionTime == 1:
    #    return maxScore
    
    penalty = 0
        
    # longer time
    penalty += successfulSubmissionTime * (maxScore / 2) * (1 / marathonLength)
    
    # wrong submissions
    penalty += (submissions - 1) * 10
    
    score = maxScore - penalty
    
    return score if score > maxScore / 2 else maxScore / 2
    