# https://app.codesignal.com/challenge/o9QW9r6JcBKqceGBq
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#def nthElementFromTheEnd(l, n):
# Run-intensive version with two list traversals
# 92
L, n = eval(dir()[0])
l = i = 0
T = L
# Find list length (1st traversal)
while T:
    l += 1
    T = T.next

#if n > l: return -1 # faster, more chars

# Find value (2nd traversal)
while i < l - n:
    L = L.next
    i += 1
#return L.value # faster, more chars
return -1 if n > l else L.value # slower, less chars


# Space-intensive version with list copy (does not feel right)
# 75
#L, n, *V = eval(dir()[0]) # *V --> V = []
#while L:
#    V += [ L.value ]
#    L = L.next
#return -1 if n > len(V) else V[-n]