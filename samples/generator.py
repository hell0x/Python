# -*- coding: utf-8 -*-
# 生成器学习

#sample1
# s = (x * x for x in range(5))
# print(s)
# for x in s:
#     print(x)
#
# # 斐波拉契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n + 1
#     return 'done'
#
# f = fib(5)
# while 1:
#     try:
#         x = next(f)
#         print('f: ', x)
#     except StopIteration as e:
#         print('Generator return value: ', e.value)
#         break

#杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0] + L
        L2 = L + [0]
        L = [L1[i]+L2[i] for i in range(len(L1))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break