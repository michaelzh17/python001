#quadratic.py

''' 
this function will return the two solutions for quadratic 
a*x**2 + b*x + c = 0 

'''

import math

def quadratic(x, y, z):
    m = (-y + math.sqrt(y**2 - 4*x*z))/(2*x)
    n = (-y - math.sqrt(y**2 - 4*x*z))/(2*x)
    return m, n