# -*- coding: utf-8 -*-

# type()函数使用

print('type(123) =', type(123))
print('type("123")', type("123"))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

import types

print(type(abs) == types.BuiltinFunctionType)
