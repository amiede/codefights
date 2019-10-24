# https://app.codesignal.com/arcade/python-arcade/yin-and-yang/NXz5g32Puypw3R97N
# XXX 
def checkPassword(attempts, password):
    def check():
        while True:
            yield (yield) == password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1