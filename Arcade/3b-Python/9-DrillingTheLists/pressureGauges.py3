# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/SkTfc263CQbGNMtoj
# https://www.w3schools.com/python/ref_func_map.asp
def pressureGauges(morning, evening):
    return [ list(map(min, morning, evening)), list(map(max, morning, evening)) ]