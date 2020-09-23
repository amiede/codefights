# https://app.codesignal.com/arcade/code-arcade/well-of-integration/mJr7vgtN4X4ecL7ZA
def timedReading(maxLength, text):
     
    return len([s for s in re.sub('[^a-zA-Z\s]', '', text).split() if len(s) <= maxLength])
