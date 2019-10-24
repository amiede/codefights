# https://app.codesignal.com/arcade/python-arcade/higher-order-thinking/CabvoEz6mpy6dJgFf
def compose(f, g):
    return lambda a: f(g(a))

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)
