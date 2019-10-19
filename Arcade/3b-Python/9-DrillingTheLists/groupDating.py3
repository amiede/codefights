# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/okcMELPg5HbvSKodi
# https://www.programiz.com/python-programming/methods/built-in/zip
# unzip --> zip(*list)
def groupDating(male, female):
    return [ [ a for a, b in zip(male, female) if a != b ] , [ b for a, b in zip(male, female) if a != b ] ] 
	#return list(zip(*[ i for i in list(zip(male,female)) if i[0] != i[1] ])) 
	#--> not working for [ [], [] ]