# -*- coding: utf-8 -*-


from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('春眠不觉晓，\n处处闻啼鸟。\n夜来风雨声，\n花落知多少。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
