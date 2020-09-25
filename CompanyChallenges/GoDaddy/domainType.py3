# https://app.codesignal.com/company-challenges/godaddy/RjJwsTCiF663krgSP
def domainType(domains):

    lookup = {
        "com" : "commercial",
        "org" : "organization",
        "net" : "network",
        "info" : "information"
    } 
    
    result = []
    for d in domains:
        result.append(lookup[d.split(".")[-1]])
        
    return result
