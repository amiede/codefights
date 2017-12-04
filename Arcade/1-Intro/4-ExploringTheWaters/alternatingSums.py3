# https://codefights.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9
def alternatingSums(a):

    # See also Python task "twoTeams" (Lurking in Lists)
    # https://codefights.com/arcade/python-arcade/lurking-in-lists/xacqXRHoHhEC3dC4N
    return [sum(a[::2]), sum(a[1::2])]