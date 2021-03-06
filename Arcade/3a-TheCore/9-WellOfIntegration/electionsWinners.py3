# https://codefights.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg
# https://app.codesignal.com/arcade/code-arcade/well-of-integration/8RiRRM3yvbuAd3MNg
def electionsWinners(votes, k):

    counter = 0
    maxVote = max(votes)
    
    # Count how many candidates could win with k extra votes
    for v in votes:
        if v + k > maxVote:
            counter += 1
    
    # Special case: None seems to be able to win
    if k == 0 and votes.count(maxVote) == 1:
        counter = 1
          
    return counter