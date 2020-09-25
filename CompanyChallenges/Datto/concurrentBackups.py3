# https://app.codesignal.com/company-challenges/datto/EqY2nxWWakbu3NTon
def concurrentBackups(threads, documents):

    # This is a makespan minimization
    # NP-hard problem for n documents 
    # (with p_j execution times)
    # and m threads
    # = (n!)^m possible schedules
    # Special case here: no schedule required! ARGH!
    # only the optimal/minimal value
    # = max{ max^n_{j=1} p_j, \sum^n_{j=1} p_j/m}
    # https://www.or.uni-bonn.de/lectures/ss10/scheduling_data/sched10_4.pdf
    
    summe = result = 0
    
    if len(documents) > 0:
        for d in documents:
            summe += d/threads
        
        summe = math.ceil(summe)
        
        # special case:
        result = max(summe, max(documents))
    
    
    return result
    