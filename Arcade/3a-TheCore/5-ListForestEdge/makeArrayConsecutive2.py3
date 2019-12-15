# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/bq2XnSr5kbHqpHGJC
# https://codefights.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
# https://app.codesignal.com/challenge/2w6tp2Lxk6T5QzZxq
def makeArrayConsecutive2(statues):
    perfectCount = max(statues) - min(statues) + 1
    
    return perfectCount - len(statues)
