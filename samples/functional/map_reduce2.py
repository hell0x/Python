# -*- coding : utf-8 -*-
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def fuc(names):
    def normalize(name):
        return name.capitalize()
    return list(map(normalize, names))

def fuc2(names):
    return list(map(lambda x: x.capitalize(), names))

L1 = ['adam', 'LISA', 'barT']
print(fuc2(L1))
