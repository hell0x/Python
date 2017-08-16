# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)

def prod2(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
