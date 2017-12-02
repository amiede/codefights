# https://codefights.com/challenge/nivKPN9nai3bMGC35
def convolutedSummary(line):
   return re.sub(r'[abcde]', lambda m: m.group(0).upper(), re.sub(r'[^abcdevwxyz]', "", line.lower()))