# -*- coding: utf-8 -*-

from operator import itemgetter

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按名字排序
print(sorted(students, key=lambda t: t[0]))
print(sorted(students, key=itemgetter(0)))

# 按成绩由低到高排序
print(sorted(students, key=lambda t: t[1]))

# 按成绩由高到低排序
print(sorted(students, key=itemgetter(1), reverse=True))