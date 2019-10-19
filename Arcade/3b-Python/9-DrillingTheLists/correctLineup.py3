# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/M6QtFEgxrfY9Wihbt
def correctLineup(athletes):
    return [ athletes[i-1] if i % 2 else athletes[i+1] for i in range(len(athletes)) ]