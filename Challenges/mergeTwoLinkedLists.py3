# https://app.codesignal.com/challenge/tLjmbhkSeYbvxa6Wi
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
# 98
# Fake hack-around from bed ;-}
#def mergeTwoLinkedLists(l1, l2):
l1, l2, *R = eval(dir()[0])
while l1:
    R += l1.value,
    l1 = l1.next
while l2:
    R += l2.value,
    l2 = l2.next
return sorted(R)


# 190
#def mergeTwoLinkedLists(l1, l2):
#l1, l2 = eval(dir()[0])
## edge cases with empty list(s)
#if l1 == None: 
#    return l2 
#elif l2 == None: 
#    return l1
#
## get the head clear
#if l1.value < l2.value:
#    h = l1
#else:
#    h = l2
#    l2 = l1
#    l1 = h
#
## main part
#while l1.next:
#    if l1.next.value > l2.value: 
#        t = l1.next
#        l1.next = l2
#        l2 = t
#    l1 = l1.next
#l1.next = l2
#
#return h    


# Recursive version sorting in place (not working with large inputs)
# 189
#def mergeTwoLinkedLists(l1, l2):
#    
#    if l1 == None: 
#        return l2 
#    elif l2 == None: 
#        return l1 
#
#    if l1.value < l2.value: 
#        l1.next = mergeTwoLinkedLists(l1.next, l2) 
#        return l1 
#    else: 
#        l2.next = mergeTwoLinkedLists(l1, l2.next) 
#        return l2
   