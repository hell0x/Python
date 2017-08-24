# -*- coding: utf-8 -*-


from datetime import datetime

with open('weixing.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('weixing.txt', 'r') as f:
    s = f.read()
    print('Open for read...')
    print(s)

with open('weixing.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
