# https://app.codesignal.com/challenge/EwvQL8R3fS9Q9ZMsC
# https://codefights.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
#def depositProfit(deposit, rate, threshold):
# Zinseszins-Formel umstellen nach Jahren
# threshold = deposit * (1 + rate/100)^years
d, r, t = eval(dir()[0])
return math.ceil(math.log10(t/d) / math.log10(1 + r/100))