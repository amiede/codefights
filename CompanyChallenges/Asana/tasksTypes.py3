# https://app.codesignal.com/company-challenges/asana/2vJMZnQzdkkhCvmxs
def tasksTypes(deadlines, day):

    result = [0] * 3
    
    for d in deadlines:
        if d <= day:
            i = 0
        elif d <= day + 7:
            i = 1
        else:
            i = 2
        
        result[i] += 1
        
    return result