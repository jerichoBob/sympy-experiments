from sympy import *

x = Symbol('x')
y = limit(sin(x)/x, x, 0)
print(x, '=', y)
print("ok")