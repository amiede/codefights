# https://app.codesignal.com/company-challenges/asana/vpDXQhiLagoaM27KL
def smartAssigning(names, statuses, projects, tasks):

    available = []
    for i, e in enumerate(statuses):        
        if e == False:
            available.append(i)
     
    if len(available) == 1:
        return names[available[0]] 
    else:
        temp = dict()
        for i in available:
            temp.update( {i : (tasks[i], projects[i] ) } )
                
        return names[min(temp, key=temp.get)]
            