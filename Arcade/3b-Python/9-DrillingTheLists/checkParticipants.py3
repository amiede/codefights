# https://app.codesignal.com/arcade/python-arcade/drilling-the-lists/iMjtcPbZpwxZazENA/
def checkParticipants(participants):
    return [ i[0] for i in enumerate(participants) if i[1] < i[0] ] 