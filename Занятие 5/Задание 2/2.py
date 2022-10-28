# -*- coding: utf-8 -*-
a = int(input())
while a <= 2:
    a = int(input())
b = 2
while a % b != 0:
    b += 1
print(b)