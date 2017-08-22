# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self):
        self.name = 'weixing'

    def __getattr__(self, item):
        if item == 'score':
            return 100
        if item == 'age':
            return lambda: 25
        raise AttributeError("'Student' object has no attribute '%s'" % item)
        # print(item)

s = Student()
print(s.name)
print(s.score)
print(s.age())
print(s.grade)
