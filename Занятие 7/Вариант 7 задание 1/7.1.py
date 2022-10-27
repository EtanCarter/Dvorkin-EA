# -*- coding: utf-8 -*-
mas=[1,2,3,4,5,6,7,8,9,10,11]
s=0
p=1
for i in range(len(mas)):
    if i % 2 == 0:
        s += mas[i]
    elif i % 2 == 1:
        p *= mas[i]
print(s)
print(p)