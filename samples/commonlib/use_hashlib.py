# -*- coding: utf-8 -*-


import hashlib

md5 = hashlib.md5()
md5.update('Hello World Wei Xing'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('Hello World'.encode('utf-8'))
sha1.update('Wei Xing'.encode('utf-8'))
print(sha1.hexdigest())
