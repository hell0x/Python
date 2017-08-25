# -*- coding: utf-8 -*-

import os


def show(path, str):
    for x in os.listdir(path):
        x = path + os.path.sep + x
        if os.path.isdir(x):
            show(x, str)
        elif os.path.basename(x).find(str) != -1:
            print(x)

show('.', 'py')
