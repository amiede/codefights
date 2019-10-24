# https://app.codesignal.com/arcade/python-arcade/higher-order-thinking/2qxqDTopmTLBnYpmC/
# XXX
def compose(functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)