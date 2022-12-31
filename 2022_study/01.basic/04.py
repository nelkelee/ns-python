
from typing import List


def plus(*num):
    v = 0
    for n in num:
        v = v + n
    print(v)


def faa(data):
    c = []
    for i in data:
        if type(i) == list:
            c+=faa(i)
        else:
            c.append(i)
    return c

plus(1,2,3,4,5)
print(faa([1,2,[3,4,5],6,7]))