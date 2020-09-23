# https://app.codesignal.com/company-challenges/purestorage/vfaESus49J4N9JHim
def longestUncorruptedSegment(sourceArray, destinationArray):

    start = rStart = 0
    length = rLength = 0
    results = []

    for i in range(len(sourceArray)):
        if sourceArray[i] == destinationArray[i]:
            if length == 0:
                start = i
            length += 1
            if length > rLength:
                rStart = start
                rLength = length
        else:
            start = length = 0
        
    return [rLength, rStart]