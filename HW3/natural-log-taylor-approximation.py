import math
import sympy as sy
import numpy as np

# Modify these variables only
center = 0
degree = 2
value = 0.2
# Modify these variables only

def taylor(x, n):
    i = 0
    p = 0
    while i <= n:
        if (i % 2 == 0):
            p = p + (x**(i+1)/(i+1))
        else:
             p = p - (x**(i+1)/(i+1))
        i += 1
    return p

taylor = taylor(value, degree - 1)
print("Taylor approximation: ", taylor)