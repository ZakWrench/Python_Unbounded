import gc
import my_module_1
from my_module_1 import pi  # explicit import
from my_module_1 import f, __g, a
from my_module_1 import *
import importlib
import sys


print(pi, my_module_1.pi)
importlib.reload(my_module_1)  # reload and execute ( exec(x) ) module

print(sys.path, '\n')

my_module_1.f(3)
a
__g(3)

print(my_module_1.area.__doc__, '\n')

my_module_2 = "my_module_2"
my_module_2 = importlib.import_module(my_module_2)
my_module_2.y()
print('')
my_module_2_attr = getattr(my_module_2, "z")
my_module_2_attr = my_module_2_attr()
my_module_2_attr

print(my_module_1.source)
# my_module_1.spect()

my_module_2.a(my_module_2.b)

print(locals().keys())

sys.modules.pop("my_module_1")
sys.modules.pop("my_module_2")
del my_module_1
del my_module_2
gc.collect()  # not always necessary
print(locals().keys(), '\n')

print(max.__doc__)
