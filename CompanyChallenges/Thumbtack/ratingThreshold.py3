# https://app.codesignal.com/company-challenges/thumbtack/eF82g2XJdkWbeWYSr
def ratingThreshold(threshold, ratings):
    
    i = 0
    review = []
    
    for p in ratings:
        if sum(p)/len(p) < threshold:
            review.append(i)
        i += 1
        
    return review