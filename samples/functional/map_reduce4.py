# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    def str2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(str2num, s.replace(".", ""))) * (10 ** (-len(s[s.index(".") + 1:])))

print('str2float(\'123.456\') =', str2float('123.456'))