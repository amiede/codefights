# VedicTwoDigitMultiplication = (a, b) ->
# Solution by miguel_r58
# 52
# [a
#  b] = args
# x = a//t=10
# j = b%t
# return [x*i = b//t
#         x*j + i*a%=t
#         a*j]

[x
 y
 _
 i
 j] = args+0
return [x*i
        x*j+y*i
        y*j]