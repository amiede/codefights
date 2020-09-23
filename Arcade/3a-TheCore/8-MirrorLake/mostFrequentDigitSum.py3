# https://app.codesignal.com/arcade/code-arcade/mirror-lake/RpoP4Aqa5mbmC8koC
def mostFrequentDigitSum(n):

    digitSum = lambda n: sum(int(digit) for digit in str(n))

    seq = [n]
    seqSums = dict()

    while n > 0:
        nSum = digitSum(n)
        seqSums[nSum] = seqSums.get(nSum, 0) + 1
        n -= digitSum(n)
        seq.append(n)
      
    # this is necessary, if there are multiple values of same occurrence
    # because only the maximum sum is needed  
    seqSums = dict(sorted(seqSums.items(), reverse=True))      
      
    print(seq,seqSums)    
    
    return max(seqSums, key=seqSums.get) 