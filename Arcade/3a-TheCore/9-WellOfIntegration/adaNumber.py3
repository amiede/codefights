# https://app.codesignal.com/arcade/code-arcade/well-of-integration/Ghe6HWhFft8h6fR49
# Solution by thelastprime
def adaNumber(line):
    line = line.replace('_', '')
    if line.isdigit(): 
        return True
    try:
        b, n = line.split('#')[:-1]
        if int(b) < 2 or int(b) > 16:
            return False
        try:
            int(n, int(b))
            return True
        except ValueError:
            return False
    except ValueError:
        return False