# https://app.codesignal.com/company-challenges/dropbox/ffibMFaS7mzKZkAE3
def incorrectPasscodeAttempts(passcode, attempts):

    threshold = 10
    incorrectAttempts = 0
    
    for a in attempts:
        if a != passcode:
            incorrectAttempts += 1
            if incorrectAttempts == threshold:
                return True
        else:
            incorrectAttempts = 0
    
    return False
