# https://app.codesignal.com/arcade/code-arcade/intro-gates/HEsmEacHr2s9wahjr
def maxMultiple(divisor, bound):

    for n in range(bound, 1, -1):
        if n % divisor == 0:
            return n