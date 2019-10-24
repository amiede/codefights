# https://app.codesignal.com/arcade/python-arcade/showing-class/pzhNXW2KrdRWyhxzR
# https://www.programiz.com/python-programming/property
class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)
    
    @property
    def area(self):
        return self.height * self.width


def primarySchool(height, width):
    return str(Rectangle(height, width))
