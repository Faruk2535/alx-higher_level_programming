#!/usr/bin/python3
"""import calculator for add, sub, mull and div of numbers"""

from calculator_1 import add, sub, mul, div

a = 1
b = 2
print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
print('{:d} + {:d} = {:d}'.format(a, b, sub(a, b)))
print('{:d} + {:d} = {:d}'.format(a, b, mul(a, b)))
print('{:d} + {:d} = {:d}'.format(a, b, div(a, b)))
