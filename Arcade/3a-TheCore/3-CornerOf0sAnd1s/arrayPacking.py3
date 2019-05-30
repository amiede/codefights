# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf
def arrayPacking(A):
     
     summe = 0
     
     # as long as there is smth to pack
     while len(A) > 0:
          # move <shift> bits to the left
          shift = 8 * (len(A)-1)
          # Remove number from the end, shift to left 
          # and add to result sumBinary OR (adding)
          summe |= A.pop() << shift
     
     return summe