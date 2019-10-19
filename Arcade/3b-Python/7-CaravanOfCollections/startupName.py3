# https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/G6yyoXW9w888pnvsZ/
# https://docs.python.org/2/library/sets.html#set-objects
def startupName(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = (cmp1 | cmp2 | cmp3) - (cmp1 ^ cmp2 ^ cmp3) # (union all) difference (symmetric difference all)
    return list(sorted(list(res)))