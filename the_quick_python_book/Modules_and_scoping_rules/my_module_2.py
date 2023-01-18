def x():
    return print("x()")


def y():
    return x()


def z():
    return y()


def a(x):
    #print("global of a(): ", globals())
    print("Entry locals of a(): ", locals())
    y = x
    print("Exit locals of a(): ", locals())


b = 2


def __g():
    return print("__g()")
