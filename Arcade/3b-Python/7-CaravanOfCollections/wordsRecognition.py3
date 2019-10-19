# https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/zmQ9DqAN2mDL9hive
def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set(w1) - set(w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]