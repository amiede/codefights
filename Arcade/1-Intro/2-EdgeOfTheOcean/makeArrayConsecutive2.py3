# https://codefights.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
def makeArrayConsecutive2(statues):
    perfectCount = max(statues) - min(statues) + 1
    
    return perfectCount - len(statues)