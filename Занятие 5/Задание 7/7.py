# Тут тоже взял предыдущую и изменил
# -*- coding: utf-8 -*-
a = int(input())
b = 0
c = a
while a != 0:
    if a > c:
        b += 1
        c = a
    a = int(input())
print(b)