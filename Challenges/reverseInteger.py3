# https://app.codesignal.com/challenge/jiDd9pPSvaLzxjZrG
#def reverseInteger(x):
# Solution by notch
# 55
reverseInteger = lambda n: int("-"*(n<0) + str(abs(n))[::-1])