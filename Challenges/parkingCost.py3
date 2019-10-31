# https://app.codesignal.com/challenge/vjsPvZ3hv5ZdxxYzC
#def parkingCost(i, o):
i,o = eval(dir()[0])
d = math.ceil((int(o[:2]) * 60 + int(o[3:]) - int(i[3:]) - int(i[:2]) * 60)/10 - 3)

p = 0

if d > 0:
    if d > 9:
        p = 9 + (d-9)*2
    else:
        p = d 

return p