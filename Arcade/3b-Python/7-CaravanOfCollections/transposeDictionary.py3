# https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/3q55u2MWA2Rw5HvmM/
# https://www.w3schools.com/python/python_dictionaries.asp
def transposeDictionary(scriptByExtension):
    return sorted( (v, k) for k, v in scriptByExtension.items() )