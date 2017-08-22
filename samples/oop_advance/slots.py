# -*- coding: utf-8 -*-


# __slots__限制实例的属性
class Student(object):
    __slots__ = ('name', 'age')     # 用tuple定义运行绑定的属性名称

class GraduateStudnet(Student):
    pass

s = Student()
s.name = 'WeiXing'
s.age = 25
# 尝试设置不在__solts__里面的属性，会报错
try:
    s.score = 100
except AttributeError as e:
    print(e)

# __solts__只限制当前类，对其子类不限制
g = GraduateStudnet()
g.score = 99
print(g.score)