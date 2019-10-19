# https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/pE4t3DcoTRfwHwYG8
# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]