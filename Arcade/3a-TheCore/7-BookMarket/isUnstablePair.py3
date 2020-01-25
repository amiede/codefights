# https://app.codesignal.com/arcade/code-arcade/book-market/Ky2mjgmxnWLi6KNPp
def isUnstablePair(filename1, filename2):
    return ( filename1 < filename2 and filename1.lower() > filename2.lower() ) or ( filename1 > filename2 and filename1.lower() < filename2.lower() )