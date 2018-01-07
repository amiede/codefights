# https://codefights.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
def depositProfit(deposit, rate, threshold):
    # Zinseszins-Formel umstellen nach Jahre
    # threshold = deposit * (1 + rate/100)^years
    return math.ceil(math.log10(threshold/deposit) / math.log10(1 + rate/100))