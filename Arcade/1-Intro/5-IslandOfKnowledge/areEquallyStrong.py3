# https://codefights.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL/
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
 minimum = min(yourLeft,yourRight) == min(friendsLeft, friendsRight)
 maximum = max(yourLeft,yourRight) == max(friendsLeft, friendsRight)
 return minimum and maximum