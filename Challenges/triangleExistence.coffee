# https://app.codesignal.com/challenge/4nwZHgbjAXTquopxR
#triangleExistence = (sides) ->
# 46
[A] = args
A.sort((a, b) => a - b)
return A[0] + A[1] > A[2]