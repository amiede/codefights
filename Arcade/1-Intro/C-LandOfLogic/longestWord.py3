# https://codefights.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma
def longestWord(text):
    # Remove non-characters, split into list, return max element(by length), done
    return max(re.sub(r"[^a-zA-Z\s]"," ",text).split(), key=len)