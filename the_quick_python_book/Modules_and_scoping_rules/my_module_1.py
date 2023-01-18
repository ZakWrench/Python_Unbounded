import importlib
import inspect
"""module example"""

pi = 3.14159


def area(r):
    """area(r): return the area of a circle with radius r."""
    # this doesn't show up in .__doc__
    global pi
    return (pi * r * r)


x = 'print("exec(x)")'
exec(x)


def f(x):
    return x


def __g(x):
    return x


a = 4
__b = 6

my_module_2 = importlib.import_module("my_module_2")
# You can use these methods to inspect any module, class, method or function.
source = inspect.getsource(my_module_2)
sourcelines, lineno = inspect.getsourcelines(my_module_2)
members = inspect.getmembers(my_module_2)

function_my_module_2, classes_my_modules_2 = inspect.getmembers(
    my_module_2, inspect.isfunction), inspect.getmembers(my_module_2, inspect.isclass)

doc_my_module_2 = inspect.getdoc(my_module_2)


def spect():
    print(f'source: {source} \n sourceline:{sourcelines} \n lineno: {lineno} \n members: {members} \n function_my_module_2: {function_my_module_2} \n classes_my_modules_2: {classes_my_modules_2} \n doc_my_module_2: {doc_my_module_2}')
