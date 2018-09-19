import math
import sympy as sy
import numpy as np

x = sy.Symbol('x')

def taylor(function, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(math.factorial(i))*(x-x0)**i
        i += 1
    return p

f = (1-x)**-1
center = 0
degree = 6
value = 0.5

absolute = f.subs(x, value)
taylor = taylor(f, center, degree).subs(x, value)

print("Absolute error: ", math.fabs(absolute - taylor))
print("Relative error: ", math.fabs((absolute - taylor) / absolute))