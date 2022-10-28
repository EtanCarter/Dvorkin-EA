# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = 1
while a < b:
    a = a + (a/100*10)
    c += 1
print(c)