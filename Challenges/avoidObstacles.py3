# https://app.codesignal.com/challenge/AEKkAcCxy9hbNWwad
#def avoidObstacles(inputArray):
I, = eval(dir()[0])
i = 3
while 1:
    if all( t % i != 0 for t in I ):
        return i
    i += 1