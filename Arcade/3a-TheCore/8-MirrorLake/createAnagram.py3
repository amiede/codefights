# https://app.codesignal.com/arcade/code-arcade/mirror-lake/BsShkFDfbkWxozmMN
from collections import Counter
def createAnagram(s, t):
    return sum((Counter(t) - Counter(s)).values())