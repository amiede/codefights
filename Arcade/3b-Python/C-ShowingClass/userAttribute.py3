# https://app.codesignal.com/arcade/python-arcade/showing-class/poBCg4uDfmXtGGiC9
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute
class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, attr):
        return "{} attribute is not defined".format(attr)
    

def userAttribute(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)
